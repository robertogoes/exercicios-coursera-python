def vogal(n):
    if n == "a" or n == "A":
        ade = True
    elif n == "e" or n == "E":
        ade = True
    elif n == "i" or n == "I":
        ade = True
    elif n == "o" or n == "O":
        ade = True
    elif n == "u" or n == "U":
        ade = True
    else:
        ade = False

    return ade

letra = input("Digite uma letra:")
n = vogal(letra)
print(n)

