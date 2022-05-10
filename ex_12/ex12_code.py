# -*- coding: utf-8 -*-
#
#  ex12_code.py
#  
#  Copyright 2022
#  Jhonata Polito Demuner
#  20221bsi0080

# Faça um programa em Python 3 para resolver o seguinte problema:
# Existem vários conjuntos de três valores reais quaisquer onde se
# deseja fazer uma estatística sobre geometria plana triangular.
# Cada conjunto de três valores reais lidos podem ou não representar
# os valores dos lados um triangulo, ou seja, os três valores reais
# lidos poderão ou não formar um triângulo. Processe estes conjuntos
# de três valores a fim de responder as perguntas a seguir e considere
# que os conjuntos de três valores encerram quando for fornecido um
# conjunto com os três valores reais iguais a zero.

#! Definição do programa principal ou função principal
def main():

    #! Declaração de variáveis
    lado1 = float (0.0)
    lado2 = float (0.0)
    lado3 = float (0.0)
    perimetro = float (0.0)
    semip = float (0.0)
    area = float (0.0)
    equicount = int (0)
    equiperimetro = float (0.0)
    escacount = int (0)
    escaperimetro = float (0.0)
    isocount = int (0)
    isoperimetro = float (0.0)
    triangulocount = int (0)
    naocount = int (0)
    maiorarea = float (0.0)
    ladomaior1 = float(0.0)
    ladomaior2 = float (0.0)
    ladomaior3 = float(0.0)
    mediaequi = float (0.0)
    mediaesca = float (0.0)
    mediaiso = float (0.0)
    perctriangulos = float (0.0)
    percnaotriangulos = float(0.0)

    maiorarea = -1

    #! Entrada de Dados
    lado1 = float(input())
    lado2 = float(input())
    lado3 = float(input())

    #! Processamento
    if lado1 == 0 and lado2 == 0 and lado3 == 0:
        print('NAO HA DADOS PARA PROCESSAR')
    else:
        while lado1 != 0 or lado2 != 0 or lado3 != 0:
            if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
                perimetro = lado1 + lado2 + lado3
                semip = perimetro / 2
                area = (semip * (semip - lado1) * (semip - lado2) * ( semip - lado3)) ** 0.5

                if lado1 == lado2 and lado2 == lado3:
                    print (f'AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = EQUILATERO')
                    equicount += 1
                    equiperimetro += perimetro
                    triangulocount += 1
                    mediaequi = equiperimetro / equicount

                elif lado1 != lado2 and lado1 != lado2 and lado3 != lado2:
                    print (f'AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = ESCALENO ')
                    escacount += 1
                    escaperimetro += perimetro
                    triangulocount += 1
                    mediaesca = escaperimetro / escacount

                else:
                    print (f'AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = ISOSCELES')
                    isocount += 1
                    isoperimetro += perimetro
                    triangulocount += 1
                    mediaiso = isoperimetro / isocount

            else:
                print('NAO TRIANGULO ')
                naocount += 1

            if area > maiorarea:
                maiorarea = area   
                ladomaior1 = lado1
                ladomaior2 = lado2
                ladomaior3 = lado3

            lado1 = float(input())
            lado2 = float(input())
            lado3 = float(input())        

        perctriangulos = triangulocount / (triangulocount + naocount) * 100
        percnaotriangulos = naocount / (triangulocount + naocount) * 100

        #! Saída
        if area != 0:
            print(f'A maior area = {maiorarea:.2f} eh do triangulo: lado1 = {ladomaior1:.2f}, lado2 = {ladomaior2:.2f} e lado3 = {ladomaior3:.2f}')
            print(f'{mediaequi:.2f} eh o perimetro medio dos triangulos equilateros')
            print(f'{mediaiso:.2f} eh o perimetro medio dos triangulos isosceles')
            print(f'{mediaesca:.2f} eh o perimetro medio dos triangulos escalenos')

        print(f'Percentual de triangulos = {perctriangulos:.2f}')
        print(f'Percentual de nao triangulos = {percnaotriangulos:.2f}')

#! Invocação(execução) do programa principal ou da função principal
if __name__ == "__main__":
    main()