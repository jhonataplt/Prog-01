# Faça uma função que receba um número inteiro positivo e retorne
# um valor boolean verdade se o número for primo e falso caso
# contrário. Um número N inteiro é considerado primo se mesmo for
# divisível somente por dois números: 1 e por ele mesmo N, e estes
# dois números são diferentes, por isso, o número 1 não é um número
# primo.
# Faça um programa principal que LEIA diversos números inteiros
# positivos, para cada número LIDO imprima próprio número somente
# uma das frases: "EH PRIMO" ou "NAO EH PRIMO". Ao final da leitura
# dos dados de entrada IMPRIMA a SOMA e o PRODUTO de todos os
# números lido que forem primos. Considere que a entrada de encerra
# quando um número menor ou igual a zero for informado pelo usuário.

import modulo

def main():

    # Declaração de variáveis
    num = int(0);
    resultado = bool;
    soma = int(0);
    produto = int(0);

    # Inicialização de variáveis
    produto = 1

    # Entrada
    num = int(input());

    # Processamento
    while num > 0:
        resultado = modulo.calcNumeroPrimo(num);
        
        # Saída
        if resultado == True:
            soma += num
            produto *= num
            print(f'{num} EH PRIMO');
        else:
            print(f'{num} NAO EH PRIMO');

        num = int(input());

    print(f'SOMA = {soma}\nPRODUTO = {produto}')

if __name__ == '__main__':
    main()