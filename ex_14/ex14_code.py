# Tem-se um conjunto de dados contendo a altura e o sexo 
# (masculino, feminino) de 50 pessoas,
# Fazer um algoritmo que calcule e escreva: a maior e a menor 
# altura do grupo, a média de altura das mulheres e o número de 
# homens.

def main():

    # Declaração de variáveis
    menorAltura = int(0)
    maiorAltura = int(0)
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
    sexo = input()

    # Processamento
    if sexo != 'm' and sexo != 'f' and sexo != 'M'and sexo != 'F':
        print('NAO HA DADOS PARA PROCESSAR')
    else: 
        while sexo == 'm' or sexo == 'f' or sexo == 'M' or sexo == 'F':

            altura = int(input())

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
            
            sexo = input()

        # Saída
        print(f'MAIOR ALTURA DO GRUPO={maiorAltura}\nMENOR ALTURA DO GRUPO={menorAltura}')
        print(f'MEDIA DA ALTURA DAS MULHERES={mediaAlturaMulheres:.1f}')
        print(f'NUMERO DE HOMENS={mcount}')

if __name__ == '__main__':
    main()