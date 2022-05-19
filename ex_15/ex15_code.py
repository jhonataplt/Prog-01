# Para cada turma será digitada a identificação da turma, número de matricula
# e a nota final. Após o último aluno de cada turma virá uma entrada que não
# corresponde a nenhum aluno, contendo zero no lugar do número de matricula.
# Deseja-se, através de um computador ler estas entradas e imprimir para cada turma,
# a sua identificação, o número de alunos aprovados, a média das notas e a melhor nota.
# Após todas as turmas serem processadas deseja-se imprimir também o total de alunos
# aprovados, a média geral e a melhor nota entre todas as turmas.
# Faça um algoritmo com essas instruções:

# ALGORITMO
#     DECLARE
#         turma {IDENTIFICAÇÃO DA TURMA}
#         mat {IDENTIFICAÇÃO DA MATRÍCULA DO ALUNO}
#         LITERAL
#     DECLARE
#         nota {IDENTIFICAÇÃO DA NOTA DO ALUNO}
#         turmaCount {QUANTIDADE DE TURMAS}
#         alunosAprovados {QUANTIDADE DE ALUNOS APROVADOS DA TURMA}
#         alunosCount {QUANTIDADE DE ALUNOS}
#         notaTotal {SOMA DA NOTA DE TODOS ALUNOS DA TURMA}
#         notaMedia {MÉDIA DA NOTA DE TODOS ALUNOS DA TURMA}
#         maiorNota {MAIOR NOTA DA TURMA}
#         totalAlunosAprovados {QUANTIDADE DE ALUNOS APROVADOS DE TODAS AS TURMAS}
#         notaGeral {SOMA DAS MÉDIAS DAS NOTAS DE TODAS AS TURMAS}
#         maiorNotaGeral {MAIOR NOTA DE TODAS AS TURMAS}
#         mediaGeral {MÉDIA DA NOTA DOS ALUNOS DE TODAS AS TURMAS}
#         NUMÉRICO
#     maiorNota ← -1
#     maiorNotaGeral ← -1
#     LEIA turma
#     SE turma = "FIM"
#         ENTAO ESCREVA "Não há dados para processar"
#         SENAO
#             ENQUANTO turma ≠ "FIM"
#                 LEIA mat
#                 turmaCount ← turmaCount + 1
#                 ENQUANTO mat ≠ "0" FAÇA
#                     LEIA nota
#                     SE nota >= 60
#                         ENTAO alunosAprovados ← alunosAprovados + 1
#                     FIM SE
#                     alunosCount ← alunosCount + 1
#                     notaTotal ← notaTotal + nota
#                     notaMedia ← notaTotal / alunosCount
#                     SE nota > maiorNota
#                         ENTAO  maiorNota ← nota
#                     FIM SE
#                     LEIA mat
#                 FIM ENQUANTO
#                 SE alunosCount = 0
#                     ENTAO ESCREVA "Turma vazia"
#                     SENAO
#                         ESCREVA turma
#                         ESCREVA alunosAprovados
#                         ESCREVA notaMedia
#                         ESCREVA maiorNota
#                     FIM SENAO
#                 FIM SE
#                 totalAlunosAprovados ← totalAlunosAprovados + alunosAprovados
#                 notaGeral ← notaGeral + notaMedia
#                 SE maiorNota > maiorNotaGeral
#                     ENTAO maiorNotaGeral ← maiorNota
#                 FIM SE
#                 alunosCount ← 0
#                 notaTotal ← 0
#                 LEIA turma
#                 ESCREVA totalAlunosAprovados
#                 ESCREVA mediaGeral
#                 ESCREVA maiorNotaGeral
#             FIM ENQUANTO
#         FIM SENAO
#     FIM SE
# FIM ALGORITMO

def main():

    # Declaração de variáveis
    turma = str('')
    mat = str('')
    nota = float(0.0)
    turmaCount = int(0)
    alunosAprovados = int(0)
    alunosCount = int(0)
    notaTotal = float(0.0)
    notaMedia = float(0.0)
    maiorNota = float(0.0)
    totalAlunosAprovados = int(0)
    notaGeral = float(0.0)
    maiorNotaGeral = float(0.0)
    mediaGeral = float(0.0)

    # Inicilaização de variáveis
    maiorNota = -1
    maiorNotaGeral = -1

    # Entrada
    turma = input()

    # Processamento
    if turma == 'FIM':
        print('Não há dados para processar')
    else:
        while turma != 'FIM':

            mat = input()
    
            turmaCount += 1

            while mat != '0':

                nota = float(input())

                if nota >= 60:
                    alunosAprovados += 1

                alunosCount += 1
                notaTotal += nota
                notaMedia = notaTotal / alunosCount

                if nota > maiorNota:
                    maiorNota = nota

                mat = input()

            if alunosCount == 0:
                print('Turma vazia')
                print('=' * 50, '\n')
            else:
                print('Turma = ', turma)
                print('Total de alunos aprovados na turma = ', alunosAprovados)
                print(f'Média das notas da turma =  {notaMedia:.2f}')
                print(f'Melhor nota da turma =  {maiorNota:.2f}')
                print('=' * 50, '\n')

            totalAlunosAprovados += alunosAprovados

            notaGeral += notaMedia

            if maiorNota > maiorNotaGeral:
                maiorNotaGeral = maiorNota

            alunosCount = 0
            notaTotal = 0            

            turma = input()

        mediaGeral = notaGeral / turmaCount

        # Saída
        print('Total e alunos aprovados na disciplina = ', totalAlunosAprovados)
        print(f'Média geral na disciplina = {mediaGeral:.2f}')
        print(f'Melhor nota da disciplina no semestre = {maiorNotaGeral:.2f}')

if __name__ == '__main__':
     main()