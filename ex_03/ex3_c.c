/* Leia SOMENTE um número inteiro e imprima uma mensagem */
/* contendo o número e um texto: PAR, se o número lido for */
/* divisível por 2 ou exclusivo IMPAR, se o número lido não for */
/* divisível por 2. */

#include <stdio.h>
#include <stdlib.h>

int main()
{
    /* Declaração de variáveis */
    int num;
    
    /* Entrada */
    printf("Insert a number here: ");
    scanf("%d", &num);
    
    /* Processamento + Saída */
    if (num % 2 != 0)
    {
        printf("%d IMPAR", num);
    }
    else
        printf("%d PAR\n", num);

    return 0;
}