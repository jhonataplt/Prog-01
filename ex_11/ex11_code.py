# Baseado no exercício 1.12.38 Livro Farrer - página 81, com 
# algumas modificações no enunciado, faça um programa em Python 
# 3. O problema proposto no exercício 1.12.38, solicita que você 
# leia o valor de x da unidade de entrada e calcule o valor de 
# exp(x) usando a série (somatório de termos de uma sequência).
# Neste programa vamos calcular o valor de exp(x) para n valores 
# de x informados pelo usuário, onde n é maior que zero e 
# representa a quantidade de valores de x que serão fornecidos 
# pelo usuário.

import math;

def main():

    # Declaração de variáveis
    n = int(0);
    x = float(0.0);
    expFunction = float(0.0);
    exp = int(0);
    fat = float(0.0);
    denominador = float(0.0);
    numerador = float(0.0);
    result = float(0.0);
    difference = float(0.0);

    # Entrada
    n = int(input());

    # Processamento
    while n > 0:

        n -= 1;
        x = float(input());
        expFunction = math.exp(x);
        difference = abs(expFunction - result);
        exp = 0;
        fat = 1;
        denominador = 1;
        numerador = x ** exp;
        result = numerador / denominador;
        
        while difference >= 0.0001:

            exp += 1;
            denominador *= fat;
            numerador = x ** exp;
            result += numerador / denominador;
            difference = abs(expFunction-result);
            fat += 1;

        # Saída
        print(f'X={x:.6f} EXP_FUNCAO({x:.6f})={expFunction:.6f} EXP_SERIE({x:.6f})={result:.6f}');

if __name__ == '__main__':
    main();