print("")
print("guzman guzman jared uziel 1188")
print("")
class Alumno:
    def __init__(self, nombre, nota):
        # Inicializa los datod del alumno del alumno
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        # Imprime los datos anteriuormente ingresados
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_resultado(self):
        # en esrta parte se muestra si dicho alumno aprobo o no
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado.")
        else:
            print(f"El alumno {self.nombre} ha suspendido.")
if __name__ == "__main__":
    
    alumno1 = Alumno("guzman guzman jared uziel ", 8.7)

    
    alumno1.imprimir_datos()
    alumno1.mostrar_resultado()
