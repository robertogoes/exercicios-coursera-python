def maior_primo(n):
    if n >= 2:
        resultado = éPrimo(n)
    else:
        resultado = str("Número menor que 2!")
    return resultado
    

def éPrimo(n):
    teste = False
    while 2 <= n and not(teste):
        aaa = calcula_primo(n)
        if aaa:
            acumulador = n
            teste = True
        n = n - 1
    return acumulador

def calcula_primo(n):
    i = 2
    contador = 1
    while i <= n:
        if n%i == 0:
            contador = contador + 1
        i = i + 1
    if contador <= 2:
        primalidade = True
    else:
        primalidade = False
    return primalidade

n = int(input("Insira um número inteiro maior ou igual a 2:"))
mostra = maior_primo(n)
print("O maior primo é:",mostra)


    

    


