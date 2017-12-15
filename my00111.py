#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

"""
sensitive_words = set()

with open (r'C:\Users\ASUS\Desktop\mingan.txt') as f:
	for w in f.readlines():
		sensitive_words.add(w.strip())

def word_filter():
	while True:
		s = input('-->')
		if s == 'exit':
			break
		if s in sensitive_words:
			print('Freedom')
		else:
			print('Human Rights')


if __name__ == '__main__':
		word_filter()



