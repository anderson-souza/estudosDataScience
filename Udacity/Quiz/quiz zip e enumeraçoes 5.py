# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:47:04 2018

@author: ander
Use enumerate para modificar a lista cast para que cada elemento contenha 
o nome seguido da altura correspondente do personagem. 
Por exemplo, o primeiro elemento de cast deve mudar 
de "Barney Stinson" para "Barney Stinson 72".
"""

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, casts in enumerate(cast):
    cast[i] = casts + " " + str(heights[i])
    

print(cast)