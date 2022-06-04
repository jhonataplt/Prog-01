def contadorFrequencia(quantidadeAlunos, contadorAusencia):
    for i in range(quantidadeAlunos):
        matricula = input();
        frequencia = input();
        
        if frequencia == 'A':
            contadorAusencia += 1;
    return contadorAusencia;

def separadorFrequencia(porcentagemFrequencia, maiorFrequencia, turmaMaiorFrequencia, menorFrequencia, turmaMenorFrequencia, identificacaoTurma, turmasAusentes):
    if porcentagemFrequencia > maiorFrequencia:
        maiorFrequencia = porcentagemFrequencia;
        turmaMaiorFrequencia = identificacaoTurma;
       
    if porcentagemFrequencia < menorFrequencia:
        menorFrequencia = porcentagemFrequencia;
        turmaMenorFrequencia = identificacaoTurma;
    
    if porcentagemFrequencia > 20:
        turmasAusentes += 1;
    
    return maiorFrequencia, turmaMaiorFrequencia, menorFrequencia, turmaMenorFrequencia, turmasAusentes;

def saida(turmaMaiorFrequencia, maiorFrequencia, turmaMenorFrequencia, menorFrequencia, turmasAusentes):
    print(f'TURMA COM MAIOR PORCENTAGEM DE AUSENCIA={turmaMaiorFrequencia} AUSENCIA={maiorFrequencia:.2f}%');
    print(f'TURMA COM MENOR PORCENTAGEM DE AUSENCIA={turmaMenorFrequencia} AUSENCIA={menorFrequencia:.2f}%');
    print(f'{turmasAusentes} TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%');