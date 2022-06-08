import modulo

def main():

    conta = str('')
    digitoVerificador = int(0)
    saldo = str('')
    nome = str('')
    validador = int(0)

    conta = input()

    if conta == '0':
        print('NÃO EXISTEM CONTAS')
    else:   
        while conta != 0:
            digitoVerificador = int(input())
            saldo = input()
            nome = input()

            validador = modulo.validador(conta);

            if validador == digitoVerificador:
                print(f'CONTA= {conta} SALDO= {saldo} NOME= {nome}  ->  VÁLIDO')
            else:
                print(f'CONTA= {conta} SALDO= {saldo} NOME= {nome}  ->  INVÁLIDO')

            conta = input()

if __name__ == '__main__':
    main()