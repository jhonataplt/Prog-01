# Faça um programa em Python3 para resolver o seguinte 
# problema: Deseja-se fazer um levantamento a respeito da 
# ausência de alunos à primeira prova de Programação de 
# Computadores para as N turmas de existentes no Ifes. O valor de 
# N é fornecido pelo usuário. O valor de N (quantidade de turmas) 
# é o primeiro dado fornecido ao usuário.

def main():
    
    # Declaração de variáveis
    n = int(0)
    ident = str('')
    quant = int(0)
    mat = str('')
    freq = str('')
    freqPerc = float(0.0)
    maiorPerc = float(0.0)
    menorPerc = float(0.0)
    turmaMaiorPerc = float(0.0)
    turmaMenorPerc = float(0.0)
    countAus = int(0)
    ausAcima = int(0)
    i = int(0)
    j = int(0)
   
    # Inicialização de variáveis
    n = int(input())
    maiorPerc = -1
    menorPerc = 101
    
    # Entrada + Processamento
    for i in range(n):
        ident = input()
        quant = int(input())
        countAus = 0
       
        for j in range(quant):
            mat = input()
            freq = input()
            
            if freq == 'A':
                countAus += 1
        
        freqPerc = countAus / quant * 100
       
        if freqPerc > maiorPerc:
            maiorPerc = freqPerc
            turmaMaiorPerc = ident
       
        if freqPerc < menorPerc:
            menorPerc = freqPerc
            turmaMenorPerc = ident
       
        if freqPerc > 20:
            ausAcima += 1
    
        # Saída
        print(f'TURMA={ident} AUSENCIA={freqPerc:.2f}%')
    print(
        f'TURMA COM MAIOR PORCENTAGEM DE AUSENCIA={turmaMaiorPerc} AUSENCIA={maiorPerc:.2f}%')
    print(
        f'TURMA COM MENOR PORCENTAGEM DE AUSENCIA={turmaMenorPerc} AUSENCIA={menorPerc:.2f}%')
    print(f'{ausAcima} TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%')
    
if __name__ == '__main__':
    main()