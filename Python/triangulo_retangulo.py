class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        self.perimetro = self.a + self.b + self.c
        return self.perimetro

    def tipo_lado(self):
        if self.a == self.b == self.c:
            resultado = "equilátero"
            return resultado
        elif (self.a != self.b) and (self.a != self.c) and (self.b != self.c):
            resultado = "escaleno"
            return resultado
        else:
            resultado = "isóceles"
            return resultado

    def retangulo(self):
        if (self.a**2 == self.b**2 + self.c**2) or (self.b**2 == self.a**2 + self.c**2) or (self.c**2 == self.a**2 + self.b**2):
            return True
        else:
            return False
