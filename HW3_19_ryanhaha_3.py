# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:45:30 2019

@author: simlab
"""

v1=0
v2=0
v3=0

v1 = (input("please enter:"))
v2 = (input("please enter:"))
v3 = (input("please enter:"))
try:
    eval(v1)
    eval(v2)
    eval(v3)
    print("Total:", float(v1)+float(v2)+float(v3))
except:
    print(v1, v2, v3)     

        