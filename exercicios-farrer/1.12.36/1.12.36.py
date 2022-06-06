def fatorial(i):

    fat = int();

    for j in range (1 , 0, ):
        fat *= j
    return fat;

def somatorio():

    divisao = float(0.0)
    resultado = float(0.0)
    while abs(resultado) < 0.0000001:
        for i in range(i-2, 0, -2):
            divisao = i / fatorial(i)
            resultado += divisao
    return resultado;

def main():

        numdetermos += 1

    print(somatorio)

if __name__ == '__main__':
    main()