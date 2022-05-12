# Produza os Algoritmos de Aposentadoria 1 e Aposentadoria 2, 
# considerando dois sexos ("m" ou "f"). Informe, também, que a 
# pessoa, também, não poderá aposentar, caso não atenda aos 
# requisitos.

def main():

    # Declaração de variáveis
    age = int(0);
    contribution = int(0);
    sum = int(0);
    genre = str ('');

    # Entrada
    genre = (input("Insert you genre: "));
    age = int(input("Insert your age: "));
    contribution = int(input("Insert your contribution time: "));
    sum = age + contribution;

    # Processamento + Saída
    if genre == 'm':
        if age >= 65:
            if contribution >= 15:
                if sum >= 95:
                    print('Can retiree');
                else: print("Can't retiree");
            else: print("Can't retiree");
        else: print("Can't retiree");

    if genre == 'f':
        if age >= 60:
            if contribution >= 15:
                if sum >= 85:
                    print('Can retiree');
                else: print("Can't retiree");
            else: print("Can't retiree");
        else: print("Can't retiree");

if __name__ == '__main__':
    main();