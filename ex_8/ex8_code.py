def main():

    #! Variable Declaration
    minitial = float(0)
    mfinal = float(0)
    hours = int(0)
    minutes = int(0)
    seconds = int(0)
    output = str('')

    #! Variable Inicialization
    minitial = float(input())

    #! Processment
    while minitial >= 0:
        mfinal = minitial
        if minitial > 0.5:
            mfinal = minitial / 2
            seconds += 50
        if minitial >= 0:

            while mfinal >= 0.5:
                mfinal /= 2
                seconds += 50
                update = (
                    f'MASSA INICIAL={round(minitial, 3)} MASSA FINAL={round(mfinal, 3)} TEMPO DECORRIDO={hours}:{minutes}:{seconds}')
            minutes = seconds // 60
            hours = seconds // 3600
            seconds %= 60
        else:
            print("FIM")
        update = (
            f'MASSA INICIAL={round(minitial, 3):.3f} MASSA FINAL={round(mfinal, 3):.3f} TEMPO DECORRIDO={hours}:{minutes}:{seconds}\n')
        output += update
        minitial = float(input())
        hours = minutes = seconds = 0

    #! Output
    print(f'{output}FIM')


if __name__ == "__main__":
    main()
#! End
