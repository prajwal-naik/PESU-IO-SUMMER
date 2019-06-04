# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:18:50 2019

@author: Prajwal
"""


a=list(input("Enter numbers").split(','));
for i in range(0, len(a)):
    a[i]=int(a[i]);
b=tuple(a);
print(b);
print(a);



