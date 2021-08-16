# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 14:15:01 2021

@author: ricar
"""

from datetime import datetime
import math

import threading
import multiprocessing

def main():
    
    qtd_cores = multiprocessing.cpu_count()
    print('realizando o processamento matemático com {} cores'.format(qtd_cores))
    
    inicio = datetime.now()
    
    threads = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * (n) / qtd_cores
        print('Core {} processando de {} até {}'.format(n, ini, fim))
        threads.append(
            threading.Thread(
                target = computar,
                kwargs = {'inicio':ini,
                          'fim':fim},
                daemon=True
            )    
        )
        
    [th.start() for th in threads]
    [th.join() for th in threads]
        
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