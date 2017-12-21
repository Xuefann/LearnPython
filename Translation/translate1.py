#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request,parse
import json
import time

def postHtml(url,data,headers):
	try:
		head = headers
		data = parse.urlencode(data).encode('utf-8')
		response = request.Request(url , headers = headers, data = data)
		toBejson = request.urlopen(response).read().decode('utf-8')
		aftjson = json.loads(toBejson)
		return aftjson
	except Exception as e:
		print('get Http Request Error: %s'%e)
		return False


print('This is Youdao Dicationary!  Welcome!')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
data = {
	'i': 'word',
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

while True:
	word = input('Please enter the text:')
	if word == 'quit':
		print('Thank you for using this script!')
		break
	else:
		data['i'] = word
		html = postHtml(url,data,headers)
		print(html['translateResult'][0][0]['tgt'])

time.sleep(2)