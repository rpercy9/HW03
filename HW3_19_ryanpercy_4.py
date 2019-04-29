#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:53:52 2019

@author: ryanpercy283
"""
v=0
while True:
    try:
        v=int(input("Please enter number:" ))
        if v % 2 == 0:
            print("even")
        if v % 2 != 0:
            print("odd")
    except:
        v!=int
        print("Not a number")