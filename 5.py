# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:12:30 2019

@author: Prajwal
"""

s=input("Enter string");
flag=0;
for i in range(len(s)):
    if ord(s[i]) in range(48,57):
        flag=flag+1;
if flag==len(s):
    print("numeric");
else:
    print("Not numeric");
    