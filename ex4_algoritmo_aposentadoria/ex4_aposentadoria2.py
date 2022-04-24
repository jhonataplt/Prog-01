def main():

    #! Variable Declaration
    idade = int(0);
    tpo_contr = int(0);
    soma = int(0);
    sexo = str ('');

    #! Input
    sexo = (input("Insert your genre here: "));
    idade = int(input("Insert your age here: "));
    tpo_contr = int(input("Insert your contribution time here: "));
    soma = idade + tpo_contr;

    #! Processment
    if sexo == 'm':
        if idade >= 65 and tpo_contr >= 15 and soma >= 95:
            print('Pode aposentar');
        else: print("Não pode aposentar");

    if sexo == 'f':
        if idade >= 60 and tpo_contr >= 15 and soma >= 85:
            print('Pode aposentar');
        else: print("Não pode aposentar");

    #! End

if __name__ == '__main__':
    main();