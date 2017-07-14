#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for
names = ['Jack','Peter','Mical']
for name in names:
    print(name)
sum = 0

# for in
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
print('sum =', sum)

#for range()
sum2 = 0
for x2 in range(101):
    sum2 += x2
print('sum2 =', sum2)

# while
sum3 = 0
x3 = 100
while x3 > 0:
    sum3 += x3
    x3 = x3 - 1
print('sum3 =', sum3)

# homework
L = ['Bart', 'Lisa', 'Adam']
for _name in L:
    print('Hello, %s!' % _name)
