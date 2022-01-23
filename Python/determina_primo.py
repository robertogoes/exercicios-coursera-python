def determina_primo(fator):
    if fator == 1:
        return False
    i = 2
    while fator%i != 0 and i <= fator/2:
        i = i + 1
    if fator%i == 0 and fator != 2:
        return False
    else:
        return True

n = int(input("Digite um inteiro positivo: "))
while n > 0:
    if determina_primo(n):
        print(n,"É primo!")
    else:
        print(n,"NÃO É PRIMO!")
    n = int(input("Digite um inteiro positivo: "))

