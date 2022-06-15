# -*- coding: utf-8 -*-
#
#  code.py
#  
#  Copyright 2022
#  Jhonata Polito Demuner
#  20221bsi0080

# Faça um programa em Python3 que:
# a) Calcule o somatório dos n primeiros termos da série definida por:
# S=1/1^3-1/3^3+1/5^3-1/7^3+1/9^3-...
# b) Calcule o valor de Pi usando a fórmula:
# pi = S×32  3
# onde o valor de S foi obtido no item a)
# c) Imprima os termos da série e os valores calculados nos itens a) e b)
# Obs.: O valor de n é um número inteiro que deverá ser informado pelo usuário e
# deverá ser checado por seu programa, para as situações a seguir:
# n <= 0 a saída impressa será N INVALIDO
# n > 0 a saída impressa será composta pelos valores calculados nos itens a) e b)
# com 5 casas decimais

import modulo

def main():

    # Declaração de variáveis
    n = int (0)
    s = float(0)

    # Entrada
    n = int(input())

    # Incialização de variáveis
    nFixo = n

    # Processamento
    if n <= 0:
        print(f'N={nFixo} N INVALIDO')
    else:
        s = modulo.calcTermos(n)
        
        pi = (s * 32) ** (1/3)

        # Saída
        print(f'N={nFixo} SOMATORIO={s:.5f} PI={pi:.5f}')
    
if __name__ == '__main__':
    main()