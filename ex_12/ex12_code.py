# Faça um programa em Python 3 para resolver o seguinte
# problema:Existem vários conjuntos de três valores reais 
# quaisquer onde se deseja fazer uma estatística sobre geometria 
# plana triangular. Cada conjunto de três valores reais lidos 
# podem ou não representar os valores dos lados um triangulo, ou 
# seja, os três valores reais lidos poderão ou não formar um 
# triângulo. Processe estes conjuntos de três valores a fim de 
# responder as perguntas a seguir e considere que os conjuntos de 
# três valores encerram quando for fornecido um conjunto com os 
# três valores reais iguais a zero.

def main():

    # Declaração de variáveis
    lado1 = float (0.0)
    lado2 = float (0.0)
    lado3 = float (0.0)
    perimetro = float (0.0)
    semip = float (0.0)
    area = float (0.0)
    equiCount = int (0)
    equiPerimetro = float (0.0)
    escaCount = int (0)
    escaPerimetro = float (0.0)
    isoCount = int (0)
    isoPerimetro = float (0.0)
    trianguloCount = int (0)
    naoCount = int (0)
    maiorArea = float (0.0)
    ladoMaior1 = float(0.0)
    ladoMaior2 = float (0.0)
    ladoMaior3 = float(0.0)
    mediaEqui = float (0.0)
    mediaEsca = float (0.0)
    mediaIso = float (0.0)
    percTriangulos = float (0.0)
    percNaoTriangulos = float(0.0)

    maiorArea = -1

    # Entrada
    lado1 = float(input())
    lado2 = float(input())
    lado3 = float(input())

    # Processamento
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
                    equiCount += 1
                    equiPerimetro += perimetro
                    trianguloCount += 1
                    mediaEqui = equiPerimetro / equiCount

                elif lado1 != lado2 and lado1 != lado2 and lado3 != lado2:
                    print (f'AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = ESCALENO ')
                    escaCount += 1
                    escaPerimetro += perimetro
                    trianguloCount += 1
                    mediaEsca = escaPerimetro / escaCount

                else:
                    print (f'AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = ISOSCELES')
                    isoCount += 1
                    isoPerimetro += perimetro
                    trianguloCount += 1
                    mediaIso = isoPerimetro / isoCount

            else:
                print('NAO TRIANGULO ')
                naoCount += 1

            if area > maiorArea:
                maiorArea = area   
                ladoMaior1 = lado1
                ladoMaior2 = lado2
                ladoMaior3 = lado3

            lado1 = float(input())
            lado2 = float(input())
            lado3 = float(input())        

        percTriangulos = trianguloCount / (trianguloCount + naoCount) * 100
        percNaoTriangulos = naoCount / (trianguloCount + naoCount) * 100

        # Saída
        if area != 0:
            print(f'A maior area = {maiorArea:.2f} eh do triangulo: lado1 = {ladoMaior1:.2f}, lado2 = {ladoMaior2:.2f} e lado3 = {ladoMaior3:.2f}')
            print(f'{mediaEqui:.2f} eh o perimetro medio dos triangulos equilateros')
            print(f'{mediaIso:.2f} eh o perimetro medio dos triangulos isosceles')
            print(f'{mediaEsca:.2f} eh o perimetro medio dos triangulos escalenos')

        print(f'Percentual de triangulos = {percTriangulos:.2f}')
        print(f'Percentual de nao triangulos = {percNaoTriangulos:.2f}')

if __name__ == "__main__":
    main()