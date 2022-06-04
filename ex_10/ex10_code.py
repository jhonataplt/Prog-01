# Resolva o exercício 1.12.18 Livro Farrer - página 81. Para o 
# caso de empate na pontuação total entre duas ou mais equipes, 
# considere como vencedora a primeira equipe lida na entrada de 
# dados.

import modulo

def main():
    
    # Declaração de variáveis
    tempoPadrao1 = float(0.0)
    tempoPadrao2 = float(0.0)
    tempoPadrao3 = float(0.0)
    tempoEquipe1 = float(0.0)
    tempoEquipe2 = float(0.0)
    tempoEquipe3 = float(0.0)
    delta1 = float(0.0)
    delta2 = float(0.0)
    delta3 = float(0.0)
    ponto1 = float(0.0)
    ponto2 = float(0.0)
    ponto3 = float(0.0)
    somaPontos = float(0.0)
    pontosVencedor = float(0.0)
    numeroInscricao = int(0)
    numeroInscricaoVencedor = int(0)
    insCount = int(0)

    # Entrada
    tempoPadrao1 = float(input())
    tempoPadrao2 = float(input())
    tempoPadrao3 = float(input())
    numeroInscricao = int(input())

    # Inicilazação de variáveis
    pontosVencedor = -1000

    # Processamento
    while numeroInscricao != 9999:
        tempoEquipe1 = float(input())
        tempoEquipe2 = float(input())
        tempoEquipe3 = float(input())
        delta1 = abs(tempoPadrao1 - tempoEquipe1)
        delta2 = abs(tempoPadrao2 - tempoEquipe2)
        delta3 = abs(tempoPadrao3 - tempoEquipe3)

        ponto1, ponto2, ponto3 = modulo.contagemPontos(delta1, delta2, delta3)
        
        somaPontos = ponto1 + ponto2 + ponto3

        if somaPontos > pontosVencedor:
            pontosVencedor = somaPontos
            numeroInscricaoVencedor = numeroInscricao
        
        print(f'EQUIPE={numeroInscricao} P1={ponto1:.2f} P2={ponto2:.2f} P3={ponto3:.2f} PT={somaPontos:.2f}')

        numeroInscricao = int(input())
        insCount += 1

    # Saída
    if insCount >= 1:
        print(f'EQUIPE VENCEDORA={numeroInscricaoVencedor} PONTUACAO TOTAL={pontosVencedor:.2f}')
    else:
        print(f'SEM EQUIPES CADASTRADAS')

if __name__ == '__main__':
    main()