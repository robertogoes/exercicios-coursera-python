def primeiro_lex(lista):
    primeiro = lista[0]
    for string in lista:
        if string < primeiro:
            primeiro = string

    return primeiro

#print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
#print(primeiro_lex(['b', 'AAAAAAA']))
