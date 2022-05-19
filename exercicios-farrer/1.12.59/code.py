def main():

    # Declaração de variáveis
    num = int(0)
    somatorio = float(0.0)
    x = float(0.0)
    delta = float(0.0)
    y1 = float(0.0)
    y2 = float (0.0)
    area = float(0.0)
    pi = float(0.0)

    # Entrada
    num = int(input())

    # Inicialização de variáveis
    somatorio = 0
    x = 0
    delta = 1/ num

    # Processamento
    while x < 1:
        y1 = 1 / (1 + x **2)
        x = x + delta
        y2 = 1 / (1 + x ** 2)
        area = ((y1 + y2) / 2) * delta
        somatorio = somatorio + area

    pi = 4 * somatorio

    # Saída
    print (pi)

if __name__  == "__main__":
    main()