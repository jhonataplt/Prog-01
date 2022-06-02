def entradas():
    candidato1 = input("Insira o nome do candidato 1: ")
    candidato2 = input("Insira o nome do candidato 2: ")
    candidato3 = input("Insira o nome do candidato 3: ")

    voto = int(input("Insira seu voto: "))
    
    return candidato1, candidato2, candidato3, voto;
# Tipos de Saída:
# candidato1, candidato2, candidato3 = str; voto = int; 

#================================================================================================================================

# Tipos de Entrada:
# voto, voto1, voto2, voto3, votoBranco, votoNulo = int;
def contagemVotos(voto, voto1, voto2, voto3, votoBranco, votoNulo):
    while voto != 0:
        if voto == 1:
            voto1 += 1
        elif voto == 2:
            voto2 += 1
        elif voto == 3:
            voto3 += 1
        elif voto == 4:
            votoBranco += 1
        elif voto == 5:
            votoNulo += 1
        else:
            print("VOTO INVALIDO")

        voto = int(input('Insira seu voto: '))

    return voto1, voto2, voto3, votoBranco, votoNulo;
# Tipos de Saída:
# voto, voto1, voto2, voto3, votoBranco, votoNulo = int;
    
#================================================================================================================================

# Tipos de Entrada:
# voto1, voto2, voto3, votoBranco = int;
def votosGeral(voto1, voto2, voto3, votoBranco):
    resultado = voto1 + voto2 + voto3 + votoBranco;
    return resultado;
# Tipos de Saída:
# voto1, voto2, voto3, votoBranco = int;

#================================================================================================================================

# Tipos de Entrada:
# voto1, voto2, voto3 = int; candidato1, candidato2, candidato3 = str;
def maisVotos(voto1, voto2, voto3, candidato1, candidato2, candidato3):
    maisVotos = -1;
    if voto1 > maisVotos:
        maisVotos = voto2
        vencedor = candidato1

    if voto2 > maisVotos:
        maisVotos = voto2
        vencedor = candidato2

    if voto3 > maisVotos:
        maisVotos = voto3
        vencedor = candidato3

    return vencedor;
# Tipos de Saída:
# voto1, voto2, voto3 = int; candidato1, candidato2, candidato3 = str;

#================================================================================================================================

# Tipos de Entrada:
# candidato1, candidato2, candidato3, vencedor = str; voto1, voto2, voto3, votoBranco, votoNulo, votosGeral = int;
def resultadoEleicao(candidato1, candidato2, candidato3, voto1, voto2, voto3, votoBranco, votoNulo, votosGeral, vencedor):
    print('=' * 70, '\n')
    print(f"O candidato {candidato1} recebeu {voto1} votos.")
    print(f"O candidato {candidato2} recebeu {voto2} votos.")
    print(f"O candidato {candidato3} recebeu {voto3} votos.")
    print('\n' + '=' * 70, '\n')
    print(f"Nessa eleição foram computados {votoBranco} votos em branco.")
    print(f"Nessa eleição foram computados {votoNulo} votos nulos.")
    print('\n' + '=' * 70, '\n')

    if votosGeral > votoNulo:
        print(f"O vencedor dessa eleição foi o candidato {vencedor}.")
    else:
        print("A eleição foi inválida pois o número de votos nulos foram maior\nque  o número de votos em candidatos e votos em branco.")

    print('\n' + '=' * 70)
    
# Tipos de Saída:
# candidato1, candidato2, candidato3, vencedor = str; voto1, voto2, voto3, votoBranco, votoNulo, votosGeral = int;