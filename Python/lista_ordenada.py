def ordenada(lista):
    tam = len(lista)
    for i in range(tam - 1):
        if lista[i] > lista[i+1]:
            return False
    return True


     
    
