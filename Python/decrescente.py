decrescente = True
anterior = int(input("Digite o primeiro valor:"))
valor = 1

while valor !=0 and decrescente:
    valor = int(input("Digite o próximo valor:"))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente == True:
    print("A sequencia de números está em ordem decrescente!")
else:
    print("A sequencia de números não está em ordem decrescente!")
