def main():

    #! Variable Declaration
    age = int(0);
    contribution = int(0);
    sum = int(0);
    genre = str ('');

    #! Input
    genre = (input("Insert you genre: "));
    age = int(input("Insert your age: "));
    contribution = int(input("Insert your contribution time: "));
    sum = age + contribution;

    #! Processment
    if genre == 'm':
        if age >= 65 and contribution >= 15 and sum >= 95:
            print('Can retiree');
        else: print("Can't retiree");

    if genre == 'f':
        if age >= 60 and contribution >= 15 and sum >= 85:
            print('Can retiree');
        else: print("Can't retiree");

    #! End

if __name__ == '__main__':
    main();