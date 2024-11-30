print("")
print("guzman guzman jared uziel 1188")
print("")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # pedimos los lados al usuario
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        # Determina poe los lAdos
        return max(self.lado1, self.lado2, self.lado3)
    
    def tipo_triangulo(self):
        # Determina el tipo de triángulo
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    
    def imprimir_informacion(self):
        # Imprime la información del triángulo
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")

lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))
triangulo = Triangulo(lado1, lado2, lado3)
# Imprimir
triangulo.imprimir_informacion()
