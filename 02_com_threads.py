# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:03:41 2021

@author: ricar
"""

import time
import colorama
from threading import Thread
from queue import Queue

def gerador_dados(queue):
    
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerdado', flush=True)
        time.sleep(2)
        queue.put(i)
        
def consumidor_de_dados(queue):
    
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dado {valor * 2} gerdado processado', flush=True)
        time.sleep(1)
        queue.task_done()
        
        
if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush = True)
    queue = Queue()
    th1 = Thread(target=gerador_dados, args=(queue,))
    th2 = Thread(target=consumidor_de_dados, args=(queue, ))
    
    th1.start()
    th1.join()
    
    th2.start()
    th2.join()