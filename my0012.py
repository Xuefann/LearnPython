# -*- coding: utf-8 -*-
"""
第 0012 题：
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
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
		for w in sensitive_words:
			if w in s:
				s = s.replace(w,'*'*len(w))
		print(s)


if __name__ == '__main__':
		
		word_filter()