def mais_curto(nomes):
    menor = nomes[0]
    menor.strip()
    for nome in nomes:
        comparado = nome.strip()
        if len(comparado) < len(menor):
            menor = comparado
            menor.lower()

    return menor.capitalize()

def testa_mais_curto():
    nomes = [" aaaa", "junior", "ANA", "IGOR"]
    print(mais_curto(nomes))
    nomes = [" AA   ", "Junior", "ANDRE", "dalva", "Bia"]
    print(mais_curto(nomes))
    nomes = ["Juanfran", "BIA", "Samora", "Wesley"]
    print(mais_curto(nomes))

    return

testa_mais_curto()
    

