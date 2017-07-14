#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
b = input('please enter your birth: ')
if int(b) < 2000:
    print('00 after')
else:
    print('before 00')
'''
h = float(input('please enter your height:'))
w = float(input('please enter your weight:'))
bmi = w / (h*h)
if bmi < 18.5:
    print('guo qing')
elif bmi >= 18.5 and bmi < 25: 
    print('zheng chang')
elif bmi >= 25 and bmi < 28: 
    print('guo zhong')
elif bmi >= 28 and bmi < 32: 
    print('fei pang')
else:
    print('yan zhong fei pang')
