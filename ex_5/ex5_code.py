# Leia três números reais quaisquer que representam os 
# coeficientes (a,b e c) de uma equação do segundo grau no 
# formato:  ax2 + bx + c = 0 
# Resolver (no domínio dos números reais) a equação do 2° grau
# se possível.

def main():

    # Declaração de variáveis

    a = float(input())
    b = float(input())
    c = float(input())

    # Processamento do delta
    if a != 0:
        delta = (b ** 2) - 4 * a * c

        # Processamento de bhaskara + Saída
        if delta >= 0:
            x1 = (-b + (delta ** 0.5)) / (2 * a)
            x2 = (-b - (delta ** 0.5)) / (2 * a)
            print("x1 = ", round(x1, 2), "\nx2 = ", round(x2, 2))
        else:
            print("Não tem solução no domínio dos números reais.")

    else:
        print("Não é equação de segundo grau.")


if __name__ == "__main__":
    main()