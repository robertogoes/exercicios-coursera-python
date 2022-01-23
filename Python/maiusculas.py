def maiusculas(frase):
    cont = len(frase) - 1
    i = 0
    frase_m = ""
    while i <= cont:
        if ord(frase[i]) < 91 and ord(frase[i]) > 64:
            frase_m += frase[i]
        i += 1

    return frase_m
