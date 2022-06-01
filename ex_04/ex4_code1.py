# Produza os Algoritmos de Aposentadoria 1 e Aposentadoria 2, 
# considerando dois sexos ("m" ou "f"). Informe, também, que a 
# pessoa, também, não poderá aposentar, caso não atenda aos 
# requisitos.

import modulo

def main():

    # Declaração de variáveis
    idade = int(0);
    contribuicao = int(0);
    sexo = str ('');
    resultado = str ('a')

    # Entrada
    sexo = input("Insira seu sexo:");
    idade = int(input("Insira sua idade: "));
    contribuicao = int(input("Insira seu tempo de contribuição: "));
    
    # Processamento
    if sexo == 'M' or sexo == 'm':
        resultado = modulo.aposentadoriaHomem(idade, contribuicao);
    elif sexo == 'F' or sexo == 'f':
        resultado = modulo.aposentadoriaMulher(idade, contribuicao);
    
    # Saída
    print(resultado)

if __name__ == '__main__':
    main();