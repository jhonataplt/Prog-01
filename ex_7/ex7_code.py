# Faça um programa em Python3 que: Leia VÁRIOS CONJUNTOS de três 
# números inteiros quaisquer (a,b e c) e para cada conjunto de 
# três números lidos imprima o maior valor entre os três valores 
# informados pelo usuário. Use como base o exemplo 1.31 resolvido 
# no livro do Farrer - pág 46.  Considere que a entra da dados 
# encerra quando os três valores inteiros fornecidos pelo usuário 
# forem todos iguais a zero.

def main():

    # Declaração de variáveis
    a = int (0);
    b = int (0);
    c = int (0);
    maior = int (0);

    # Entrada
    a = int(input());
    b = int(input());
    c = int(input());

    # Processamento
    if a > b:
        if a > c:
            maior = a;
        else: maior = c;          
    else:
        if b > c:
            maior = b;
        else: maior = c;   

    while a != 0 or b != 0 or c != 0:
        
        # Saída
        print(f"MAIOR ({a}, {b}, {c}) = {maior}\n");
        
        # Entrada
        a = int(input());
        b = int(input());
        c = int(input());
        
        # Processamento
        if a > b:
            if a > c:
                maior = a;
            else: maior = c;
        else:
            if b > c:
                maior = b;
            else: maior = c;
                
if __name__ == "__main__":
    main()