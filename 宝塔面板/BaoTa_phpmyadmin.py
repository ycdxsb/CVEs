# https://my.oschina.net/Harveysn0w/blog/4525709
import requests
import sys

domain = sys.argv[1]
payload = ':888/pma'
url = domain+payload

response = requests.get(url)
if response.status_code == 200:
    print("漏洞存在！")
else:
    print("可能不存在")