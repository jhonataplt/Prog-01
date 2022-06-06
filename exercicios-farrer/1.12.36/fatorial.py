def fatorial(i):

    fat = int(1);

    for j in range (i , 0, -1):
        fat *= j
    return fat;

def somatorio(i):

    divisao = float(0.0)
    resultado = float(0.0)
    
    for i in range(i, 0, -1):
        divisao = i / fatorial(i)
        resultado += divisao
    return resultado;

def main():

    i = int (0)
    i = int(input())

    print (somatorio(i))

if __name__ == '__main__':
    main()