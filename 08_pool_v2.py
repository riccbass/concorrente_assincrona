# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:22:06 2021

@author: ricar
"""


import multiprocessing

def calcular(dado):
    
    return dado ** 2

def imprimir_nome_processo():
    
    print(f'Iniciando o processo com o nome: ', multiprocessing.current_process().name)
    
    with open(r"C:\programacao_assincrona\test.txt", "a") as myfile:
        myfile.write(multiprocessing.current_process().name + '\n')

def main():
    
    tamanho_pool = multiprocessing.cpu_count() * 2
    print(tamanho_pool)
    
    pool = multiprocessing.Pool(processes = tamanho_pool, 
                                initializer=imprimir_nome_processo) #initializer executa para cada processo criado
    
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)
    
    print('Saídas: ', saidas)
    
    pool.close()
    pool.join()
    
    
if __name__ == '__main__':
    main()
