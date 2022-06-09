def calcTermos (numerador, denominador, n):
    s = int(0)
    
    while n > 0:
        termo = numerador / denominador ** 3
        s += termo
        print(f'{numerador}/{denominador}^3')
        denominador += 2
        numerador *= -1
        n -= 1

    return s;