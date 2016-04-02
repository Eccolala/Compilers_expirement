# -*- coding: utf-8 -*-
from Tkinter import *
import re

#define lists
num = []
char = []

def isNum(ch):
    if re.search(r'\d',ch):
        return True
    return False

def isChar(ch):
    ch_list = re.findall(r'[a-z]',ch)
    if len(ch_list) != 0:
        return True
    else:
        return False

#string_in = raw_input('Please input a sentence : ')
testString = 'a  bc@#12@#3$'


for ch in testString:
    if isNum(ch):
        num.append(ch)
    elif isChar(ch):
        char.append(ch)

print '整数 ：' ,num
print '字母 ：',char

