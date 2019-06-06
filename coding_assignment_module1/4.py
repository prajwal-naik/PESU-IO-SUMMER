# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:04:59 2019

@author: Prajwal
"""


n=int(input("Enter number"));
sum=0;
while(n!=0):
    sum=sum+(n%10);
    n=int(n/10);
print("Sum is", sum);
