def validadorCpf (cpf):
    soma = int(0)
    peso = int(2)
    resultado = int(0)

    for i in range(len(cpf)-2, 10, 1):
        soma += int(cpf[i]) * peso
        peso += 1
        resto = soma % 11
        validador = 11 - resto

        if validador == int(cpf[i]):
            resultado +=1

    return resultado;