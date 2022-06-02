import modulo

def main():

    candidato1 = str("")
    candidato2 = str("")
    candidato3 = str("")
    voto = int(0)
    voto1 = int(0)
    voto2 = int(0)
    voto3 = int(0)
    votoBranco = int(0)
    votoNulo = int(0)
    votosGeral = int(0)
    vencedor = str("")

    candidato1, candidato2, candidato3, voto = modulo.entradas(); 

    voto1, voto2, voto3, votoBranco, votoNulo = modulo.contagemVotos(voto, voto1, voto2, voto3, votoBranco, votoNulo)
      
    vencedor = modulo.maisVotos(voto1, voto2, voto3, candidato1, candidato2, candidato3);

    votosGeral = modulo.votosGeral(voto1, voto2, voto3, votoBranco);

    modulo.resultadoEleicao(candidato1, candidato2, candidato3, voto1, voto2, voto3, votoBranco, votoNulo, votosGeral, vencedor);

if __name__ == '__main__':
    main()
