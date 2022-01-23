# n**2 = i**2 + j**2
def soma_hipotenusas(n):
    somador = 0
    x = 1 
    while x <= n:
        hipotenusa = é_hipotenusa(x)
        if hipotenusa == 0:
            x = x + 1
        else:
            somador = somador + x
            x = x + 1
    return somador

def é_hipotenusa(num):
    i = j = 1
    while i < j + num:
        while j < i + num:
            if num**2 == i**2 + j**2:
                return num
            else:
                j = j + 1
        i = i + 1
        j = 1
    return 0
