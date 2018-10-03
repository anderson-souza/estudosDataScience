# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:00:43 2018

@author: ander
Use uma compreensão de listas para criar uma nova lista first_names, 
que contém apenas os primeiros nomes em names em letras minúsculas.
"""

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name[:name.find(' ')].lower() for name in names]
print(first_names)