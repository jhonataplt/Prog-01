# Tem-se um conjunto de dados contendo a altura e o sexo 
# (masculino, feminino) de 50 pessoas.
# Fazer um algoritmo que calcule e escreva: a maior e a menor 
# altura do grupo, a média de altura das mulheres e o número de 
# homens
# 
# ALGORITMO
#     DECLARE 
#         menorAltura {MENOR ALTURA DO GRUPO}
#         maiorAltura {MAIOR ALTURA DO GRUPO}
#         altura {IDENTIFICAÇÃO DE ALTURA}
#         mcount {NÚMERO DE HOMENS}
#         fcount {NÚMERO DE MULHERES}
#         faltura {SOMA DA ALTURA DE TODAS AS MULHERES}
#         mediaAlturaMulheres {MÉDIA DE ALTURA DE TODAS AS MULHERES}
#         NUMERICO
#     DECLARE 
#         sexo {IDENTIFICAÇÃO DE SEXO}
#         LITERAL
#     menorAltura ← 10000
#     maiorAltura ← -1
#     LEIA quantpessoas
#     SE quantpessoas = 0
#         ENTAO ESCREVA "NAO HÁ DADOS PARA PROCESSAR"
#         SENAO
#             ENQUANTO quantpessoas ≠ 0 FAÇA
#                 LEIA sexo
#                 LEIA altura        
#                 quantpessoas ← quantpessoas - 1              
#                 SE altura > maiorAltura
#                     ENTAO
#                         maiorAltura ← altura
#                     SENÃO 
#                         SE altura < menorAltura
#                             menorAltura ← altura
#                         FIM SE
#                     FIM SENAO
#                 FIM SE          
#                 SE sexo = "m"
#                     ENTAO
#                         mcount ← mcount + 1
#                     SENAO
#                         SE sexo = "f"
#                             fcount ← fcount + 1
#                             faltura ← faltura + altura
#                             mediaAlturaMulheres ← faltura / fcount
#                         FIM SE
#                     FIM SENAO
#                 FIM SE
#                 LEIA sexo
#             FIM ENQUANTO
#             ESCREVA maiorAltura, menorAltura
#             ESCREVA mediaAlturaMulheres
#             ESCREVA mcount
#         FIM SENAO
#     FIM SE
# FIM ALGORITMO          
            
def main():

    # Declaração de variáveis
    menorAltura = int(0)
    maiorAltura = int(0)
    quantpessoas = int(0)
    sexo = str ('')
    altura = int(0)
    mcount = int (0)
    fcount = int (0)
    faltura = int(0)
    mediaAlturaMulheres = float (0.0)

    # Inicilaização de variáveis
    menorAltura = 10000
    maiorAltura = -1

    # Entrada
    quantpessoas = int(input())

    # Processamento
    if quantpessoas == 0:
        print('NAO HA DADOS PARA PROCESSAR')
    else: 
        while quantpessoas != 0:

            sexo = input()
            altura = int(input()) 

            quantpessoas -= 1

            if altura > maiorAltura:
                maiorAltura = altura
            else:
                if altura < menorAltura:
                    menorAltura = altura
            
            if sexo == 'm' or sexo == 'M':
                mcount += 1
            else:
                if sexo == 'f' or sexo == 'F':
                    fcount += 1
                    faltura += altura
                    mediaAlturaMulheres = faltura / fcount           

        # Saída
        print(f'MAIOR ALTURA DO GRUPO={maiorAltura}\nMENOR ALTURA DO GRUPO={menorAltura}')
        print(f'MEDIA DA ALTURA DAS MULHERES={mediaAlturaMulheres:.1f}')
        print(f'NUMERO DE HOMENS={mcount}')

if __name__ == '__main__':
    main()