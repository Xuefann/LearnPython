# -*- coding: utf-8 -*-

from urllib import request
import os


def url_open(url):
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
	req = request.Request(url, headers = headers)
	response = request.urlopen(req)
	html = response.read()
	return html


def get_page(url):
	html = url_open(url).decode('utf-8')
	a = html.find('current-comment-page')+23
	b = html.find(']',a)
	return html[a:b]

def find_imgs(url):
	html = url_open(url).decode('utf-8')	
	img = addrs = []
	img_addrs = []
	a = html.find('img src=')

	while a != -1:
		b = html.find('.jpg',a,a+255)
		if b != -1:
			img_addrs.append(html[a+9:b+4])
		else:
			b = a+9

		a = html.find('img src=',b)

	for each in img_addrs:
		print(each)
	return img_addrs


def save_imgs(folder,img_addrs):
	for each in img_addrs:
		filename = each.split('/')[-1]
		with open(filename,'wb') as f:
			img = url_open(each)
			f.write(img)


def download_mm(folder = 'mm', pages = 10):
	if not os.path.isdir(folder):
		os.mkdir(folder)
	os.chdir(folder)

	url = "http://jandan.net/ooxx/"
	page_num = int(get_page(url))
		
	for i in range(pages):
		page_num -= 1
		page_url = url+'page-'+str(page_num)+'#comments'
		img_addrs = find_imgs(page_url)
		save_imgs(folder,img_addrs)

if __name__ == '__main__':
	download_mm()