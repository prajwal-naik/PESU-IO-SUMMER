# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:46:27 2019

@author: Prajwal
"""


n=int(input("Enter number "));
sum=0;
while(n!=0):
    sum=sum+int(n%10);
    n=int(n/10);
print("Sum is ", sum);