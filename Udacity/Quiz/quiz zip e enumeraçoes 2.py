# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:35:17 2018

@author: ander

Use zip para criar um dicionário cast que usa names como chave e heights como valores.
"""

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)