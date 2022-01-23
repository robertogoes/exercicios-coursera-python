import math

a = int(input("Insira o valor de a:"))
b = int(input("Insira o valor de b:"))
c = int(input("Insira o valor de c:"))

delta = (b**2)-(4*a*c)

if delta < 0:
      print("O delta é negativo, não existem raizes reais!")
elif delta == 0:
      x = ((-b)/(2*a))
      print("As raízes existem e são iguais a", x)
else:
      x1 = (-b+math.sqrt(delta))/(2*a)
      x2 = (-b-math.sqrt(delta))/(2*a)
      print("As raizes são",x1," e",x2,"!")
