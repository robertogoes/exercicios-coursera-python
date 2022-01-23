n = int(input("Digite um número inteiro:"))
somador = 0
while n != 0:
    somador = somador + n%10
    n = n//10
print(somador)
