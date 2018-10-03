# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 01:53:27 2018

@author: ander
Quiz: Chunker
Se você tem um iterável que é grande demais para caber na memória por completo 
(ex. ao lidar com arquivos grandes), ser capaz de pegar e utilizar apenas
pedaços a cada vez pode ser muito valioso.

Implemente uma função de gerador, chunker, que recebe um iterável e retorna 
um pedaço de tamanho específico por vez.

Recorrendo à função assim:

for chunk in chunker(range(25), 4):
    print(list(chunk))
deve resultar na saída:

[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
"""

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))