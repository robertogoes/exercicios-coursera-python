import pytest
def busca_binaria_recur(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria_recur(lista, elemento, min, meio-1)

    elif lista[meio] < elemento:
        return busca_binaria_recur(lista, elemento, meio+1, max)

    else:
        return meio

a = [10, 20, 30, 40, 50, 60]

@pytest.mark.parametrize("lista, valor, esperado", [
    (a, 10, 0),
    (a, 30, 2),
    (a, 20, 1),
    (a, 40, 3),
    (a, 60, 5),
    (a, 50, 4),
    (a, 45, False),
    (a, 70, False),
    (a, -10, False)
    ])

def testa_busca_binaria_recursivo(lista, valor, esperado):
    assert busca_binaria_recur(lista, valor) == esperado
