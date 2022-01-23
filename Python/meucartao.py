meucartao = int(input("Digite o número do seu CC:"))
cartaolido = 1
encontreiccnalista = False

while cartaolido != 0 and not(encontreiccnalista):
    cartaolido = int(input("Digite o próximo número de cartão de crédito!"))
    if cartaolido == meucartao:
        encontreiccnalista = True

if encontreiccnalista:
    print("O cartão foi encontrado!")
else:
    print("O cartão não está na lista!")
