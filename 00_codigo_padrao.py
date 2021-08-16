# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:15:01 2021

@author: ricar
"""

from datetime import datetime
import math

def main():
    inicio = datetime.now()
    
    computar(fim=50_000_000)
    
    tempo = datetime.now() - inicio
    
    print('Terminou em: {} segundos'.format(tempo.total_seconds()))
    
def computar(fim, inicio = 1):
    
    pos = inicio 
    fator = 1000 * 1000
    
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))
        
if __name__ == '__main__':
    main()

'''
Terminou em: 10.270269 segundos
'''