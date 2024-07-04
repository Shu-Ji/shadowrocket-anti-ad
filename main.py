# coding: u8

import re
from datetime import datetime, timezone, timedelta
from string import Template
import httpx


tz_utc_8 = timezone(timedelta(hours=8))
build_time = datetime.now(tz=tz_utc_8).strftime("%Y-%m-%d")


def download_from_anti_ad():
    """https://github.com/privacy-protection-tools/anti-AD"""

    url = 'https://anti-ad.net/surge.txt'
    rules = httpx.get(url).content.decode('u8')
    rules = re.sub(r'DOMAIN-SUFFIX,(.*)', r'DOMAIN-SUFFIX,\1,REJECT', rules)
    return rules


def download_from_neodevhost():
    """https://github.com/neodevpro/neodevhost"""

    res = []
    url = 'https://neodev.team/lite_domain'
    rules = httpx.get(url).content.decode('u8').splitlines()
    for rule in rules:
        if rule and not rule.startswith('#'):
            res.append(f'DOMAIN-SUFFIX,{rule},REJECT')
    return '\n'.join(res)


rules = download_from_anti_ad()
# rules = download_from_neodevhost()

tmp = Template(open('./sr-template.conf').read())
rules = tmp.substitute(build_time=build_time, rules=rules)

open('./rules/sr-anti-ad.conf', 'w').write(rules)
