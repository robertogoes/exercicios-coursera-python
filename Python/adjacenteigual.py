n = int(input("Digite o valor a ser avaliado:"))
ac1 = n%10
achouadjacente = False
n = n//10

while n !=0 and not(achouadjacente):
    ac2 = n%10
    if ac2 == ac1:
        achouadjacente = True
    n = n//10
    ac1 = ac2

if achouadjacente:
    print("Nesse número há dois números adjacentes!")
else:
    print("Nesse número não há dois números adjacentes!")
    
    
