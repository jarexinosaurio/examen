print("")
print("guzman jared;1188")
print("")
#abrimos clase llamada persona
class Persona:
    def __init__(self, nombre="", edad=19, dni=""):
        self.nombre = nombre
        self.edad = edad


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = value

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def esMayorDeEdad(self):
        return self.edad >= 18

try:
    persona = Persona(nombre="Jared")
    print(persona.mostrar())
    print("Es mayor de edad:", persona.esMayorDeEdad())
except ValueError as e:
    print(e)