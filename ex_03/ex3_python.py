# Leia SOMENTE um número inteiro e imprima uma mensagem contendo 
# o número e um texto: PAR, se o número lido for divisível por 2 
# ou exclusivo IMPAR, se o número lido não for divisível por 2.

def main():

    # Declaração de Variáveis
    num = int(0)

    # Entrada
    num = int(input("Insert a number here: "))

    # Processamento + Saída
    if num % 2 != 0:
        print(num, "IMPAR")
    else:
        print(num, "PAR")

if __name__ == '__main__':
    main()
