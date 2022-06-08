def validador(conta):
    soma = int(0)
    peso = int(2)
    
    for i in range(len(conta)-1, -1, -1):
        soma += int(conta[i]) * peso
        peso += 1

    resto = soma % 11
    validador = 11 - resto

    return validador;