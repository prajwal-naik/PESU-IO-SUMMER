# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:26:44 2019

@author: Prajwal
"""


a=input("Enter numbers separated by commas ").split(',')
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
ele=int(input("Enter search element "))
beg=0
end=len(a);
pos=-1
while(beg<end):
    m=int((beg+(end-1))/2)
    if a[m]==ele:
        pos=m;  break;
    elif ele<a[m]:
        end=m-1
    else:
        beg=m+1
if pos>=0:
    print("Element is present at ", pos)
else:
    print("Element is not present at all")
    