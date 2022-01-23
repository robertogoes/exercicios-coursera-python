def n_primos(n):
    i = 2
    somador = 0
    while i <= n:
        j = 2
        while i%j != 0 and i != j:
            j = j + 1 
        if i%j == 0 and i == j:
            somador = somador + 1
        elif i%j == 0:
            somador = somador + 0
        else:
            somador = somador + 1
        i = i + 1

    return somador 
