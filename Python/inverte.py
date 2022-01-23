lista = []
num = int(input())
while num != 0:
    lista.append(num)
    num = int(input())
    
i = len(lista)-1
while i >= 0:
    print(lista[i])
    i = i - 1 
    
    

