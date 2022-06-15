def calcTermos (n):
    denominador = int(1)
    numerador = int(1)
    s = int(0)
    
    for i in range(n, 0, -1):
        termo = numerador / denominador ** 3
        s += termo
        print(f'{numerador}/{denominador}^3')
        denominador += 2
        numerador *= -1

    return s;