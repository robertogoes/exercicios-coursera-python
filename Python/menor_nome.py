def menor_nome(nomes):
    menor = nomes[0]
    menor.strip()
    for nome in nomes:
        comparado = nome.strip()
        if len(comparado) < len(menor):
            menor = comparado
            menor.lower()

    return menor.capitalize()
