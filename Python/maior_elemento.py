def maior_elemento(lista):
    comparador = -9999
    for item in lista:
        if item > comparador:
            comparador = item

    return comparador
