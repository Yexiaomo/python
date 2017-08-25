#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

print('\n---math库---\n')
print('math.pi = %f' % math.pi)
print('math.e = %f' % math.e)
print('ceil(1.5) = %f' % math.ceil(1.5))
print('floor(1.5) = %f' % math.floor(1.5))
print('pow(2,3) = %f' % math.pow(2,3))
print('log(%f) = %f' % (math.e, math.log(math.e)))
print('log10(10) = %f' % math.log10(10))
print('math.exp(1) = %f' % math.exp(1))
print('math.sqrt(8) = %f' % math.sqrt(8))
print('degrees(3.1415926) = %f' % math.degrees(3.1415926))
print('radians(180) = %f' % math.radians(180))
print('sin(30) = %f' % math.sin( math.radians(30)))

print('\n---random库---\n')
print('random(): %f' % random.random())
print('uniform(1,10): %f' % random.uniform(1,10))
print('randint(1,10): %f' % random.randint(1,10))