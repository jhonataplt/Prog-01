# Faça um programa em Python3 que leia dois números inteiros 
# quaisquer. Calcule a divisão inteira do primeiro pelo segundo 
# sem utilizar os operadores aritméticos /, // ou % em nenhuma 
# parte de seu código.

def main():

    # Declaração de variáveis
    num = int(0)
    div = int(0)
    result = int(0)

    # Entrada
    num = int(input())
    div = int(input())

    # Processamento + Saída
    if num > 0 and div > 0:
        while num >= div:
            num -= div
            result += 1
        print(f"QUOCIENTE={result }")
    else:
        print("ENTRADA INVALIDA")

if __name__ == "__main__":
    main()