# soma dos elementos de uma lista

def soma_lista(lista):
    if len(lista) <= 1:
        return lista[0]
    resultado = lista[0] + soma_lista(lista[1:]) 
    
    return  resultado

    
