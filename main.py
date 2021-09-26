# coding: u8

import re
from datetime import datetime
from string import Template
from urllib import request

build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

url = 'https://anti-ad.net/surge.txt'
rules = request.urlopen(url).read().decode('u8')
rules = re.sub(r'DOMAIN-SUFFIX,(.*)', r'DOMAIN-SUFFIX,\1,REJECT', rules)

tmp = Template(open('./sr-template.conf').read())
rules = tmp.substitute(build_time=build_time, anti_ad_rules=rules)

open('./sr-anti-ad.conf', 'w').write(rules)
