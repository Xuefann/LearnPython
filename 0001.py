#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？

"""
import random

def creat_num(long):
	str = 'qwertyuiopasdfghjklzxcvnm1234567890'
	a = ''
	for j in range(long):
		a += random.choice(str)

	return a



f = open('keys1.txt','w')
for i in range(200):
	f.write(str(creat_num(10))+'\n')

f.close()
