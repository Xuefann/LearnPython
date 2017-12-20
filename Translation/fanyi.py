
from urllib import request,parse
import json

word = input('-->input:')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
data = {
	'i': word,
	'from':'AUTO',
	'to':'AUTO',
	'smartresult':'dict',
	'client':'fanyideskweb',
	'salt':'1513777498355',
	'sign':'d39d6328f657afd1e6c806f84695c020',
	'doctype':'json',
	'version':'2.1',
	'keyfrom':'fanyi.web',
	'action':'FY_BY_CLICKBUTTION',
	'typoResult':'false'}



data = parse.urlencode(data).encode('utf-8')
req = request.Request(url,headers = headers,data = data)
page = request.urlopen(req).read().decode('utf-8')
target = json.loads(page)

print(target['translateResult'][0][0]['tgt'])