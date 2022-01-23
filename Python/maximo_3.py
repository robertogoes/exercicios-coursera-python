def maximo(v1,v2,v3):
    if (v1>v2 and v1>v3) or (v1>v2 and v2==v3):
        resultado = v1
    elif (v2>v1 and v2>v3) or (v2>v3 and v1==v3):
        resultado = v2
    elif (v3>v1 and v3>v2) or (v3>v1 and v2==v1):
        resultado = v3
    elif v1==v2==v3:
        resultado = v1
    return resultado

v1 = int(input("Digite o 1 valor:"))
v2 = int(input("Digite o 2 valor:"))
v3 = int(input("Digite o 3 valor:"))
n = maximo(v1, v2, v3)
print(n)
