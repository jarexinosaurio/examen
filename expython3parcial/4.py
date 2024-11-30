print("")
print("guzman guzman jared uziel 1188")
print("")
class Calculadora:
    def __init__(self, num1, num2):
        # inicia los dos numeros a usar
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        # realizar la suma
        return self.num1 + self.num2

    def resta(self):
        # realizar la resta
        return self.num1 - self.num2

    def multiplicacion(self):
        # realizar la multiplicación
        return self.num1 * self.num2

    def division(self):
        # realizar la división
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

# Solicitar 
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
calculadora = Calculadora(num1, num2)
# imprime los resultados
print(f"La suma de {num1} y {num2} es: {calculadora.suma()}")
print(f"La resta de {num1} y {num2} es: {calculadora.resta()}")
print(f"La multiplicación de {num1} y {num2} es: {calculadora.multiplicacion()}")
print(f"La división de {num1} y {num2} es: {calculadora.division()}")
