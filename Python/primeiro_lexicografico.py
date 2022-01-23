def menor_string(array_nomes):
    primeiro = array_nomes[0]
    for nome in array_nomes:
        nome = nome.lower()
        primeiro = primeiro.lower()
        if str(nome) < str(primeiro):
            primeiro = nome

    return primeiro

def testa_menor():
    menor = ["amanda", "julia", "ANA", "morela", "andy"]
    print(menor_string(menor))
    menor = ["Roberto", "joeliza", "jo", "Dalva", "Andre"]
    print(menor_string(menor))
    menor = ["Denelizio", "Rai", "Cundy", "liz", "buente"]
    print(menor_string(menor))

    return

testa_menor()
