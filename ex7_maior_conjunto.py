def main():

    #! Variable Declarations
    a = int (0);
    b = int (0);
    c = int (0);
    maior = int (0);
    output = str("");

    #! Input
    a = int(input());
    b = int(input());
    c = int(input());

    #! Processment
    if a > b:
        if a > c:
            maior = a;
        else:
            maior = c;
    else:
        if b > c:
            maior = b;
        else:
            maior = c;

    while a != 0 or b != 0 or c != 0:
        
        update = (f"MAIOR ({a}, {b}, {c}) = {maior}\n");
        output += update;
        
        #! Input
        a = int(input());
        b = int(input());
        c = int(input());
        
        #! Processment
        if a > b:
            if a > c:
                maior = a;
            else:
               maior = c;
        else:
            if b > c:
                maior = b;
            else:
                maior = c;
                
    #! Input
    print (output);


if __name__ == "__main__":
    main()
#! End