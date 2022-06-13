def calcNumeroPrimo(num):

    resultado = bool;
    possiveisDivisores = int(0);

    resultado = False;

    if num != 1:
        possiveisDivisores = 0;
        
        for i in range(1, 200):
            if num % i == 0:
                possiveisDivisores += 1;
        if possiveisDivisores == 2:
            resultado = True;
            
    return resultado;