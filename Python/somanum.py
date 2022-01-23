n = int(input("Insira o valor que os digitos devem ser somados:"))
somador = 0

while n != 0:
    somador = somador + (n%10)
    n = n//10
print("O valor da soma é:",somador)
    
    
