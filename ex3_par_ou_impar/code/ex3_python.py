def main():
    #! Variable Declaration + Input
    num = int(input("Insert a number here: "))

    #! Data Processment + Output
    if num % 2 != 0:
        print(num, "IMPAR")
    else:
        print(num, "PAR")

#! End
if __name__ == '__main__':
    main()
