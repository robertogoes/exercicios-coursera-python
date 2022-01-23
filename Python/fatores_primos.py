def determina_primo(fator):
    resultado = i = 1  
    while i <= n:
        if fator%i == 0:
            resultado = resultado + 1
        i = i + 1
    if resultado > 3:
        resultado = True
    else:
        resultado = False
    return resultado 



n = int(input("Digite um número inteiro > 1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("fator ", fator, "multiplicidade = ", multiplicidade)
    multiplicidade = 0
    fator = fator + 1

