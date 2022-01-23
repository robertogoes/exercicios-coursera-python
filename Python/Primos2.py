def é_primo(n):
    fator = 2
    if x == 2:
        return True

    while n % fator != 0 and fator <= n/2:
        fator = fator + 1
    if n % fator == 0:
        return False
    else:
        return True


valor_limite = int(input("Limite máximo: "))

x = 2
while x < valor_limite:
    if é_primo(x):
        print(x, end=", ")
    x = x + 1
