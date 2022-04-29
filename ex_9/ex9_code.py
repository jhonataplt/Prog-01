def main():
    
    #! Declaração de Variáveis
    n = int(0)
    ident = str('')
    quant = int(0)
    mat = str('')
    freq = str('')
    freqperc = float(0.0)
    maiorperc = float(0.0)
    menorperc = float(0.0)
    turmamaiorperc = float(0.0)
    turmamenorperc = float(0.0)
    countaus = int(0)
    ausacima = int(0)
    i = int(0)
    j = int(0)
   
    #! Inicialização de Variáveis
    n = int(input())
    maiorperc = -1
    menorperc = 101
    
    #! Entrada de dados + Processamento
    for i in range(n):
        ident = input()
        quant = int(input())
        countaus = 0
       
        for j in range(quant):
            mat = input()
            freq = input()
            
            if freq == 'A':
                countaus += 1
        
        freqperc = countaus / quant * 100
       
        if freqperc > maiorperc:
            maiorperc = freqperc
            turmamaiorperc = ident
       
        if freqperc < menorperc:
            menorperc = freqperc
            turmamenorperc = ident
       
        if freqperc > 20:
            ausacima += 1
    
        #! Saída de Dados
        print(f'TURMA={ident} AUSENCIA={freqperc:.2f}%')
    print(
        f'TURMA COM MAIOR PORCENTAGEM DE AUSENCIA={turmamaiorperc} AUSENCIA={maiorperc:.2f}%')
    print(
        f'TURMA COM MENOR PORCENTAGEM DE AUSENCIA={turmamenorperc} AUSENCIA={menorperc:.2f}%')
    print(f'{ausacima} TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%')
    
if __name__ == '__main__':
    main()
#! End
