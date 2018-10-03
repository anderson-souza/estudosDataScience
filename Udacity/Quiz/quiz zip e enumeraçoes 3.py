# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:36:56 2018

@author: ander

Descompacte a tupla cast em duas tuplas, names e heights.
"""

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)