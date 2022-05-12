# Resolva o exercício 1.12.18 Livro Farrer - página 81. Para o 
# caso de empate na pontuação total entre duas ou mais equipes, 
# considere como vencedora a primeira equipe lida na entrada de 
# dados.

def main():
    
    # Declaração de variáveis
    tp1 = float(0.0)
    tp2 = float(0.0)
    tp3 = float(0.0)
    te1 = float(0.0)
    te2 = float(0.0)
    te3 = float(0.0)
    delta1 = float(0.0)
    delta2 = float(0.0)
    delta3 = float(0.0)
    pt1 = float(0.0)
    pt2 = float(0.0)
    pt3 = float(0.0)
    pt = float(0.0)
    ptVenc = float(0.0)
    nins = int(0)
    ninsVenc = int(0)
    insCount = int(0)

    #! Input
    tp1 = float(input())
    tp2 = float(input())
    tp3 = float(input())
    nins = int(input())
    ptVenc = -1000

    #! Processment
    while nins != 9999:
        te1 = float(input())
        te2 = float(input())
        te3 = float(input())
        delta1 = abs(tp1 - te1)
        delta2 = abs(tp2 - te2)
        delta3 = abs(tp3 - te3)

        if delta1 < 3:
            pt1 = 100
        else:
            if delta1 >= 3 and delta1 <= 5:
                pt1 = 80
            else:
                pt1 = 80 - (delta1 - 5) / 5

        if delta2 < 3:
            pt2 = 100
        else:
            if delta2 >= 3 and delta2 <= 5:
                pt2 = 80
            else:
                pt2 = 80 - (delta2 - 5) / 5

        if delta3 < 3:
            pt3 = 100
        else:
            if delta3 >= 3 and delta3 <= 5:
                pt3 = 80
            else:
                pt3 = 80 - (delta3 - 5) / 5
        
        pt = pt1 + pt2 + pt3

        if pt > ptVenc:
            ptVenc = pt
            ninsVenc = nins
        
        print(f'EQUIPE={nins} P1={pt1:.2f} P2={pt2:.2f} P3={pt3:.2f} PT={pt:.2f}')

        nins = int(input())
        insCount += 1

    #! Output
    if insCount >= 1:
        print(f'EQUIPE VENCEDORA={ninsVenc} PONTUACAO TOTAL={ptVenc:.2f}')
    else:
        print(f'SEM EQUIPES CADASTRADAS')

if __name__ == '__main__':
    main()