# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 2017
@author: simmihacks
"""
#this program converts numbers into binary
num = 
#give your own value of num

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ' '
if num == 0:
    result = '0' 
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '~' + result
#make sure to type 'result' in the Python Console
