# Faça um programa em Python3 para resolver o seguinte 
# problema: Um material radioativo perde a metade de sua massa 
# inicial a cada 50 segundos. Faça um programa que leia diversas 
# massas iniciais todas maiores que zero, para cada massa inicial 
# lida calcule a quantidade de segundos necessárias para que o 
# valor da massa inicial se torne menor que 0,5.

def main():

    # Declaração de variáveis
    mInitial = float(0)
    mFinal = float(0)
    hours = int(0)
    minutes = int(0)
    seconds = int(0)
    output = str('')

    # Inicialização de  variável
    mInitial = float(input())

    # Processamento
    while mInitial >= 0:
        mFinal = mInitial
        if mInitial > 0.5:
            mFinal = mInitial / 2
            seconds += 50
        if mInitial >= 0:

            while mFinal >= 0.5:
                mFinal /= 2
                seconds += 50
                update = (
                    f'MASSA INICIAL={round(mInitial, 3)} MASSA FINAL={round(mFinal, 3)} TEMPO DECORRIDO={hours}:{minutes}:{seconds}')
            minutes = seconds // 60
            hours = seconds // 3600
            seconds %= 60
        else:
            print("FIM")
        update = (
            f'MASSA INICIAL={round(mInitial, 3):.3f} MASSA FINAL={round(mFinal, 3):.3f} TEMPO DECORRIDO={hours}:{minutes}:{seconds}\n')
        output += update
        mInitial = float(input())
        hours = minutes = seconds = 0

    # Saída
    print(f'{output}FIM')


if __name__ == "__main__":
    main()