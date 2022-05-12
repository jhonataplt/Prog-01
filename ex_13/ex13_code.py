# Programa que leia diversos números inteiros maiores ou iguais
# a zero na base 10, calcule e imprima o equivalente deste
# número na base 16, As entradas e saídas deste programa devem
# ser feitas no programa principal (função main). A conversão do
# número lido na base 10 para seu respectivo valor na base 16 
# deverá ser implementada/codificada por você programador. Não é
# permitido o uso de formatação da apresentação do número em 
# hexadecimal e não é permitido o uso de nenhum comando/função já
# existem tem Python para realizar a conversão do número da base 
# 10 para a base 16.

def main():

    # Declaração de variáveis
    b10 = int(0)
    b10Final = int (0)
    quociente = int(0)
    resto = int (0)
    b16 = str ('')

    # Entrada de dados
    b10 = int(input())

    # Processamento
    while b10 >= 0:
        
        b10Final = b10

        if b10 == 0:
            b16 = '0'

        else:
            while b10 != 0:

                quociente = b10 // 16
                resto = b10 % 16

                if resto >= 10:
                    if resto == 10:
                        b16 = 'A' + b16
                    if resto == 11:
                        b16 = 'B' + b16
                    if resto == 12:
                        b16 = 'C' + b16
                    if resto == 13:
                        b16 = 'D' + b16
                    if resto == 14:
                        b16 = 'E' + b16
                    if resto == 15:
                        b16 = 'F' + b16
                else:
                    b16 = str (resto) + b16
                
                b10 = quociente

        # Saída
        print(f'BASE10={b10Final} BASE16={b16}')

        b10 = int(input())

        b16 = ''

if __name__ == '__main__':
    main()