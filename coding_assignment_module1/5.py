# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:49:22 2019

@author: Prajwal
"""


s=input("Enter string ");
flag=0;
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        flag=flag+1;
if(flag==len(s)):
    print("The entered string is a numeric");
else:
    print("The enetered string is not a numeric");
