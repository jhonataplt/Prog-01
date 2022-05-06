import math;

def main():

    #! Variable Declaration
    n = int(0);
    x = float(0.0);
    expfunction = float(0.0);
    exp = int(0);
    fat = float(0.0);
    denominador = float(0.0);
    numerador = float(0.0);
    result = float(0.0);
    difference = float(0.0);

    #! Input
    n = int(input());

    #! Processment
    while n > 0:

        n -= 1;
        x = float(input());
        expfunction = math.exp(x);
        difference = abs(expfunction - result);
        exp = 0;
        fat = 1;
        denominador = 1;
        numerador = x ** exp;
        result = numerador / denominador;
        
        while difference >= 0.0001:

            exp += 1;
            denominador *= fat;
            numerador = x ** exp;
            result += numerador / denominador;
            difference = abs(expfunction-result);
            fat += 1;

        #! Output
        print(f'X={x:.6f} EXP_FUNCAO({x:.6f})={expfunction:.6f} EXP_SERIE({x:.6f})={result:.6f}');

if __name__ == '__main__':
    main();