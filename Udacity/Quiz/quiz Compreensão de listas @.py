# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:01:48 2018

@author: ander
Use uma compreensão de lista para criar uma lista de nomes passed, 
que só incluem aqueles que marcaram pelo menos 65 pontos.
"""

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = passed = [name for name, score in scores.items() if score >= 65]
print(passed)