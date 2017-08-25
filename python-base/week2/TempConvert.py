#!/usr/bin/env python3
# -*- coding: utf-8 -*-

val = input("Please enter temperature value with a temperature symbol (e.g.: 32C): ")
if val[-1] in ['c','C']:
	f = 1.8 * float(val[0:-1]) +32
	print("After convert temperature is %.2fF" % f)
elif val[-1] in ['f','F']:
	c = (float(val[0:1]) - 32) / 1.8
	print("After convert temperature is %.2fC" % c)
else:
	print('Input is error!')