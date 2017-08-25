#! /usr/bin/env python3
# -*- coding: utf-8 -*-

sum, tmp = 0, 1
for i in range(1,11):
	tmp *= i
	sum += tmp
print('1!+2!+...+10! =',sum)