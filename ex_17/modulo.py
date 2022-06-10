def conversorDecinalHexadecimal(b10):
    quociente = int(0)
    resto = int(0)
    b16 = str('')

    if b10 == 0:
            b16 = '0'

    else:
        while b10 != 0:

            quociente = b10 // 16
            resto = b10 % 16

            if resto >= 10:
                if resto == 10:
                    b16 = 'A' + b16
                if resto == 11:
                    b16 = 'B' + b16
                if resto == 12:
                    b16 = 'C' + b16
                if resto == 13:
                    b16 = 'D' + b16
                if resto == 14:
                    b16 = 'E' + b16
                if resto == 15:
                    b16 = 'F' + b16
            else:
                b16 = str (resto) + b16

            b10 = quociente

    return b16;