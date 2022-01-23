def insertion_sort(lista):
    fim = len(lista)

    for i in range(fim-1):
        for j in range(i+1, 0, -1):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]

    return lista         
    
