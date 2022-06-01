# Leia três números reais quaisquer que representam os 
# coeficientes (a,b e c) de uma equação do segundo grau no 
# formato:  ax2 + bx + c = 0 
# Resolver (no domínio dos números reais) a equação do 2° grau
# se possível.

import modulo;

def main():

    # Declaração de variáveis
    a = float(0.0)
    b = float(0.0)
    c = float(0.0)
    delta = float(0.0)
    # x1 = float(0.0)
    # x2 = float(0.0)

    # Entrada
    a = float(input())
    b = float(input())
    c = float(input())

    # Processamento
    if a != 0:
        delta = modulo.delta(a, b, c);

        if delta >= 0:
            x1 = modulo.bhaskarax1(delta, a, b);
            x2 = modulo.bhaskarax2(delta, a, b);

            # Saída
            print(f"x1 = {x1:.2f} \nx2 = {x2:.2f}")
        else:
            print("Não tem solução no domínio dos números reais.")

    else:
        print("Não é equação de segundo grau.")


if __name__ == "__main__":
    main()