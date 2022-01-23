import random
def lista_grande(n):
    lista = []
    i = 0
    while i < n:
        lista.append(random.randint(0, 100))
        i += 1

    return lista
