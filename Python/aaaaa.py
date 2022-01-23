def fatorial(n):
    i = acum = 1
    while i <= n:
        acum = i*acum
        i = i + 1
        print(acum)
    return acum

n = int(input("Digite um número inteiro para calcular fatorial:"))
while n >= 0:
    resultado = fatorial(n)
    print("O FATORIAL DO NÚMERO QUE VOCÊ DIGITOU É: ", resultado)
    n = int(input("Digite um número inteiro para calcular fatorial:"))
print("Você não digitou um inteiro positivo!")


