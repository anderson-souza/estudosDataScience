# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 01:46:28 2018

@author: ander

screva sua própria função de gerador que funciona como a função interna enumerate.

Recorrendo à função assim:

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
deve resultar na saída:

Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
"""

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    i = start
    for element in iterable:
        yield i, element
        i += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))