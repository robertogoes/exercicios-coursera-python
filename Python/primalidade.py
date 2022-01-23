n = int(input("Digite um número inteiro:"))
i = 1
somador = 0

while i < n:
    if n%i == 0:
        somador = somador + 1
    i = i + 1

if somador > 1:
    print("não primo")
elif n ==1:
    print("não primo")
else:
    print("primo")
        
        
    
