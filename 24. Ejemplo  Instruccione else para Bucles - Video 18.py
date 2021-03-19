# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:38:29 2020

@author: JARBY II
"""

email=input('Introduce tu email: ')
for i in email:
    if i == '@':
        arroba=True
        break;
        
else:
    arroba=False

print(arroba)
