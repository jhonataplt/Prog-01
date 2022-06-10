# Faça um programa em Python3 para resolver o seguinte problema:
# - Programa que leia diversos números inteiros maiores ou iguais a
# zero na base 10, calcule e imprima o equivalente deste número na
# base 16, As entradas e saídas deste programa devem ser feitas no
# programa principal (função main). A conversão do número lido na
# base 10 para seu respectivo valor na base 16 deverá ser feita por
# uma função definida por você programador.

import modulo

def main():

    # Declaração de variáveis
    b10 = int(0)
    b16 = str ('')

    # Entrada de dados
    b10 = int(input())

    # Processamento
    while b10 >= 0:
     
        b16 = modulo.conversorDecinalHexadecimal(b10);

        # Saída
        print(f'BASE10={b10} BASE16={b16}')

        b10 = int(input())

        b16 = ''

if __name__ == '__main__':
    main()