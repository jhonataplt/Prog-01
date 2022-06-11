def mdc (num1, num2):
    
    menorNum = int (100000000000000);
    divisor = int (0);
    mdc = int(1);

    if num1 < menorNum:
        menorNum = num1;

    if num2 < menorNum:
        menorNum = num2;

    while num1 != 1 and num2 != 1:
        for divisor in range (2, menorNum + 1):
            if num1 % divisor == 0 or num2 % divisor == 0:
                while num1 % divisor == 0 or num2 % divisor == 0:

                    if num1 % divisor == 0 and num2 % divisor == 0:
                        mdc *= divisor;

                    if num1 % divisor == 0:
                        num1 /= divisor;

                    if num2 % divisor == 0:
                        num2 /= divisor;

    return mdc;

