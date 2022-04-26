def main():

    #! Variable Declaration
    num = int(0)
    div = int(0)
    result = int(0)

    #! Input
    num = int(input())
    div = int(input())

    #! Processment + Output
    if num > 0 and div > 0:
        while num >= div:
            num -= div
            result += 1
        print(f"QUOCIENTE={result }")
    else:
        print("ENTRADA INVALIDA")


if __name__ == "__main__":
    main()
#! End