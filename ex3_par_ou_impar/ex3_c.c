/*
! Import Libraries */
#include <stdio.h>
#include <stdlib.h>
/*
! General Process */
int main()
{
    /*
    ! Variable Declaration */
    int num;
    /*
    ! Input */
    printf("Insert a number here: ");
    scanf("%d", &num);
    /*
    ! Data Processment + Output */
    if (num % 2 != 0)
    {
        printf("%d IMPAR", num);
    }
    else
        printf("%d PAR", num);
}
/*
! End */