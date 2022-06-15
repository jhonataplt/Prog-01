# -*- coding: utf-8 -*-
#
#  code.py
#  
#  Copyright 2022
#  Jhonata Polito Demuner 
#  20221bsi0080
#
# Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES) para resolver
# o seguinte problema:
# a) Definir uma função em Python 3 que calcule o valor da área do triângulo formado entre uma reta,
# definida pela equação y = ax + b, e os eixos coordenados (eixo X e eixo Y). Esta função recebe como
# parâmetros os valores de a e b que definem a equação y = ax + b. Esta função retorna o valor da área
# calculada do triângulo formado.
# Atenção: se o valor de a ou o valor de b for igual a zero, não há formação de um triângulo entre a reta
# y = ax + b e os eixos coordenados (X e Y). Neste caso o valor retornado por esta função para a área
# calculada deverá ser ZERO.
# b) Faça um programa principal que leia diversos pares de valores que representam os coeficientes (a e b)
# da reta y = ax + b. Para cada par (a, b) de valores lidos imprima uma saída EXATAMENTE conforme o modelo
# apresentado nos casos de teste abaixo. A condição de parada é que os valores fornecidos para a e b sejam
# ambos iguais a zero.

import modulo

# Função com o programa principal
def main():

    # Declaração de vriáveis
    a = float(0.0)
    b = float(0.0)
    area = float(0.0)
    
    # Entrada
    a = float(input())
    b = float(input())

    # Processaento
    while a != 0 or b != 0:
        area = modulo.calcAreaTriangulo(a, b)

        # Saída
        print(f'AREA={abs(area):.5f} A={a:.5f} B={b:.5f}')
        
        a = float(input())
        b = float(input())


    

# Fim da função main

# Invocação/chamada do programa principal
if __name__ == '__main__':
    main()

# Fim