# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:20:07 2019

@author: Prajwal
"""


a=input("Enter numbers separated by commas ").split(',');
for i in range(len(a)):
    a[i]=int(a[i]);
print("The list is ", a);
b=tuple(a);
print("The tuple is ", b);
