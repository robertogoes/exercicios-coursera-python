# Encontrando ímpares em uma lista

def encontra_impares(lista, lista_impares = None):
    if lista_impares == None:
        lista_impares = []
    if len(lista) < 1:
        return []
    else:
        if lista[0]%2 != 0:
            lista_impares.extend([lista[0]])
        encontra_impares(lista[1:], lista_impares)        

    return lista_impares
