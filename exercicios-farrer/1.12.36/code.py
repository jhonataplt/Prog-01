def main():
    denominador = int(1);
    numerador = int(0)
    contadorTermos = int(0)
    resultado = int(0)
    fatorial = int(0)
    numerador = 63
    resultadoParcial = numerador/denominador

    while abs(resultadoParcial)>=0.0000001:
        for j in range (fatorial, 1, -1):
            denominador *= j
        fatorial += 1
        contadorTermos += 1
        resultadoParcial = numerador / denominador
        resultado += resultadoParcial
        numerador -= 2

    print(f'Somatório = {resultado}')
    print(f'Número de termos = {contadorTermos}')

if __name__ == '__main__':
    main()