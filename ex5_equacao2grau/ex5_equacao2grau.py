def main():

    #! Variable Declaration

    a = float(input())
    b = float(input())
    c = float(input())

    #! Delta Processment
    if a != 0:
        delta = (b ** 2) - 4 * a * c

        #! Bhaskara Processment
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

#! End
