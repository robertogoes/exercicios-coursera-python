larg = int(input("Digite a largura: "))
alt = int(input("Digite a altura: "))
i = j = 1
while j <= alt:
    i = 1
    while i <= larg:
        if alt%j == 0 or alt%j != 0 and (i == 1 or i == larg):
            print("#", end = "")
        else:
            print(" ", end = "") 
        i = i + 1
    print()
    j = j + 1


