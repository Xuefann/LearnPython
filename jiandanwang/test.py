# -*- coding: utf-8 -*-

from urllib import request
import os


def url_open():
	url='http://jandan.net/ooxx/page-396#comments'
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
	req = request.Request(url, headers = headers)
	response = request.urlopen(req)
	html = response.read().decode('utf-8')
	print(html)

if __name__ == '__main__':
	url_open()