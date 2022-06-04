# Faça um programa em Python3 para resolver o seguinte 
# problema: Deseja-se fazer um levantamento a respeito da 
# ausência de alunos à primeira prova de Programação de 
# Computadores para as N turmas existentes no Ifes. O valor de 
# N é fornecido pelo usuário. O valor de N (quantidade de turmas) 
# é o primeiro dado fornecido ao usuário.

import modulo

def main():
    
    # Declaração de variáveis
    numeroTurmas = int(0);
    identificacaoTurma = str('');
    quantidadeAlunos = int(0);
    porcentagemFrequencia = float(0.0);
    maiorFrequencia = float(0.0);
    menorFrequencia = float(0.0);
    turmaMaiorFrequencia = float(0.0);
    turmaMenorFrequencia = float(0.0);
    contadorAusencia = int(0);
    turmasAusentes = int(0);
   
    # Entrada
    numeroTurmas = int(input());

    # Inicialização de variáveis
    maiorFrequencia = -1;
    menorFrequencia = 101;
    
    # Entrada + Processamento
    for i in range(numeroTurmas):
        identificacaoTurma = input();
        quantidadeAlunos = int(input());
        contadorAusencia = 0;
       
        contadorAusencia = modulo.contadorFrequencia(quantidadeAlunos, contadorAusencia);
        
        porcentagemFrequencia = contadorAusencia / quantidadeAlunos * 100
       
        maiorFrequencia, turmaMaiorFrequencia, menorFrequencia, turmaMenorFrequencia, turmasAusentes = modulo.separadorFrequencia(
            porcentagemFrequencia, maiorFrequencia, turmaMaiorFrequencia, menorFrequencia, turmaMenorFrequencia, identificacaoTurma, turmasAusentes)
    
        # Saída
        print(f'TURMA={identificacaoTurma} AUSENCIA={porcentagemFrequencia:.2f}%')

    modulo.saida(turmaMaiorFrequencia, maiorFrequencia, turmaMenorFrequencia, menorFrequencia, turmasAusentes)
    
if __name__ == '__main__':
    main()