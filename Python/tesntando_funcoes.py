print("Computador começa!")
n = 20
m = 15
maior_multiplo = 0
i = 2
jogada = 0
while i <= n:
    if ((m+1)%i == 0) and (n-i > m):
        maior_multiplo = i
        print((m+1)%i)
        print(i)
        
    i = i + 1
print(maior_multiplo)

    
