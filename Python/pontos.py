import math
n1 = int(input("Digite o 1o numero:"))
n2 = int(input("Digite o 2o numero:"))
n3 = int(input("Digite o 3o numero:"))
n4 = int(input("Digite o 4o numero:"))
d = math.sqrt(((n1-n3)**2)+((n2-n4)**2))
if (d >= 10):
    print("longe")
else:
    if (d < 10):
        print("perto")
