# coding: u8

import re
from datetime import datetime, timezone, timedelta
from string import Template
import httpx

tz_utc_8 = timezone(timedelta(hours=8))
build_time = datetime.now(tz=tz_utc_8).strftime("%Y-%m-%d %H:%M:%S")

url = 'https://anti-ad.net/surge.txt'
rules = httpx.get(url).content.decode('u8')
rules = re.sub(r'DOMAIN-SUFFIX,(.*)', r'DOMAIN-SUFFIX,\1,REJECT', rules)

tmp = Template(open('./sr-template.conf').read())
rules = tmp.substitute(build_time=build_time, anti_ad_rules=rules)

open('./rules/sr-anti-ad.conf', 'w').write(rules)
