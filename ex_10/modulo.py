def contagemPontos(delta1, delta2, delta3):
    if delta1 < 3:
        ponto1 = 100
    else:
        if delta1 >= 3 and delta1 <= 5:
            ponto1 = 80;
        else:
            ponto1 = 80 - (delta1 - 5) / 5;

    if delta2 < 3:
        ponto2 = 100;
    else:
        if delta2 >= 3 and delta2 <= 5:
            ponto2 = 80;
        else:
            ponto2 = 80 - (delta2 - 5) / 5;

    if delta3 < 3:
        ponto3 = 100;
    else:
        if delta3 >= 3 and delta3 <= 5:
            ponto3 = 80;
        else:
            ponto3 = 80 - (delta3 - 5) / 5;
    
    return ponto1, ponto2, ponto3;