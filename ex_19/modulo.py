def calcNumeroPrimo(num):

    possiveisDivisores = int(0);

    if num != 1:
        possiveisDivisores = 0;
        
        for i in range(1, num + 1):
            if num % i == 0:
                possiveisDivisores += 1;
            
    return True if possiveisDivisores == 2 else False;