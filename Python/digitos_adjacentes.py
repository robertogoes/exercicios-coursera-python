n = int(input("Digite um número inteiro:"))
ac1 = n%10
achouadjacente = False
n = n//10
while n !=0 and not(achouadjacente):
    ac2 = n%10
    if ac1 == ac2:
        achouadjacente = True
    n = n//10
    ac1 = ac2
if achouadjacente:
    print("sim")
else:
    print("não")
