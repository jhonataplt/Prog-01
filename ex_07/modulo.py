def maior(a, b, c):
    if a > b:
        if a > c:
            maior = a;
        else: maior = c;          
    else:
        if b > c:
            maior = b;
        else: maior = c;
    return maior;