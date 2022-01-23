def ordena(lista):
    tam = len(lista)
    for i in range(0, tam-1):
        numero_vez = i
        for j in range(i+1, tam):
            if lista[j] < lista[numero_vez]:
                numero_vez = j

        lista[i], lista[numero_vez] = lista[numero_vez], lista[i]

    return lista
    
