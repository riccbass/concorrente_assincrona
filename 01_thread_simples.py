# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:30:17 2021

@author: ricar
"""

import threading #1
import time


def main():
    
    th = threading.Thread(target=contar, args=('elefante', 10))    #2
    th.start() # adiciona a thread na pool na thread prontas para a execução #3
    print('podemos fazer outras coisas no programa enquanto a thread vai executando')
    print('Geek university ' * 2)
    
    th.join() #avisa para ficar executando aqui enquanto a thead está executando #4
    
    print('pronto!')
    
    
def contar(o_que, numero):
    
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)
        
if __name__ == '__main__':
    main()