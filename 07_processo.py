# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:22:06 2021

@author: ricar
"""

import multiprocessing

print('iniciando o processo com nome: ', multiprocessing.current_process().name)


def faz_algo(valor):
    
    print('fazendo algo com o ', valor)
    
def main():
    
    pc = multiprocessing.Process(target=faz_algo, args=('Passáro',), name='Processo RVB')
    
    print('iniciando processo com nome: ', pc.name)
    
    pc.start()
    pc.join()
    
if __name__ == '__main__':
    main()
