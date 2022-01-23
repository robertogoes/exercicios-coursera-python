import math

class bhaskara:
 
      def delta(self, a,b,c):
            return (b**2)-(4*a*c)

      def main(self):
            aDigitado = float(input("Insira o valor de a:"))
            bDigitado = float(input("Insira o valor de b:"))
            cDigitado = float(input("Insira o valor de c:"))
            print(self.calcula_raizes(aDigitado, bDigitado ,cDigitado))

      def calcula_raizes(self, a,b,c):
            d = self.delta(a,b,c)
            if d < 0:
                  return 0
            elif d == 0:
                  x = ((-b+math.sqrt(d))/(2*a))
                  return 1, x
            else:
                x1 = (-b+math.sqrt(d))/(2*a)
                x2 = (-b-math.sqrt(d))/(2*a)
                return 2, x1, x2
                if x2 > x1:
                  print("as raízes da equação são",x1,"e",x2)
                else:
                    print("as raízes da equação são",x2,"e",x1)

