# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:31:01 2019

@author: Prajwal
"""


a=list(input("Enter numbers separated by spaces").split(' '));
for i in range(len(a)):
    a[i]=int(a[i]);
    
ele=int(input("Enter element")); 
pos=-1;    
beg=0;
end=len(a)-1;
while(end>beg):
    m=int((beg+(end-1))/2);
    if a[m]==ele:
        pos=m; break;
    elif(ele>a[m]):
        beg=m+1;
    else:
        end=m-1;
        
if(pos>=0):
    print("Element is present at ", pos);
else:
    print("Element is not present");
    
    