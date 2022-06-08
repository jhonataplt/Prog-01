import modulo

def main():

    nome = str('')
    cpf = str('')
    resultado = int(0)

    nome = input()
    
    while nome != '':
        cpf = input()

        resultado = modulo.validadorCpf(cpf)

        if resultado == 2:
            print(f'NOME= {nome} CPF= {cpf}  ->  VÁLIDO')
        else:
            print(f'NOME= {nome} CPF= {cpf}  ->  VÁLIDO')

        nome = input()

if __name__ == '__main__':
    main()