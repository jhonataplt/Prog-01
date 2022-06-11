# Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E
# USANDO SUAS PRÓPRIAS FUNÇÕES) para resolver o seguinte problema:
# a) Definir uma função em Python 3 que calcule o valor do máximo
# divisor comum (mdc) entre dois números inteiros positivos. Esta
# função recebe como parâmetro dois números inteiros positivos e
# retorna o valor do mdc calculado. Para realizar o cálculo do
# máximo divisor comum entre dois números utilize o algoritmo de
# Euclides (deixei um video explicativo) aqui em nossa sala do AVA.
# b) Faça um programa principal que leia 25 conjuntos com 3
# números inteiros positivos. Para cada conjunto de três números
# lidos, imprima os números lidos na ordem em que foram lidos e o
# valor do mdc calculado. A saída deste programa deverá ser
# EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo.
# c) Invocar o programa principal.

import modulo

def main():

    # Declaração de variáveis
    num1 = int(0)
    num2 = int(0)
    num3 = int (0)
    num1Fixo = str('')
    num2Fixo = str('')
    num3Fixo = str('')
    mdc = int(0)

    for i in range(25):
    # Entrada
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())

        # Inicialização de vriáveis
        num1Fixo = num1
        num2Fixo = num2
        num3Fixo = num3
        mdc = 1

        # Processamento
        mdc = modulo.mdc(num1, num2)
        mdc = modulo.mdc(mdc, num3)

        # Saída
        print(f'MDC({num1Fixo}, {num2Fixo}, {num3Fixo})={mdc}')

if __name__ == '__main__':
    main()