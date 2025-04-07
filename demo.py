class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def area (self):
        return self.lado * self.lado

lado = int(input("Ingrese el lado"))
ejemplo = Cuadrado (lado)
r = ejemplo.area()
print(f"el area es {r}")

