# Faça um programa em Python3 para resolver o seguinte 
# problema: Um material radioativo perde a metade de sua massa 
# inicial a cada 50 segundos. Faça um programa que leia diversas 
# massas iniciais todas maiores que zero, para cada massa inicial 
# lida calcule a quantidade de segundos necessárias para que o 
# valor da massa inicial se torne menor que 0,5.

import modulo

def main():

    # Declaração de variáveis
    massaInicial = float(0)
    massaFinal = float(0)
    segundos = int(0)
    tempoDecorrido = str('')

    # Entrada
    massaInicial = float(input())

    # Processamento
    while massaInicial >= 0:
        massaFinal = massaInicial

        if massaInicial >= 0:
            massaFinal, segundos = modulo.divisor(massaFinal, segundos);
            tempoDecorrido = modulo.conversorDeSegundos(segundos)

        print(f'MASSA INICIAL={massaInicial:.3f} MASSA FINAL={massaFinal:.3f} TEMPO DECORRIDO={tempoDecorrido}')
        massaInicial = float(input())
        segundos = 0

    # Saída
    print('FIM')

if __name__ == "__main__":
    main()