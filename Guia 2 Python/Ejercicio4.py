# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:41:59 2020

@author: Sebastian
"""

a=0
r=8
i=0
for a in range(r):
    a=a+1
    i=i+a
    if(r==a):
        print(a,"=",i)
        break 
    print(a,'+ ',end='') 