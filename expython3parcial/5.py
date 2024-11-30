print("")
print("guzman guzman jared uziel 1188")
print("")
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Ingresa el nombre de tu contacto: ")
        telefono = input("Ingrese el teléfono tu contacto: ")
        email = input("Ingrese el email del contacto que deseas agregar: ")
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email
        }
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos registrados.")
        else:
            for idx, contacto in enumerate(self.contactos, start=1):
                print(f"{idx}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

    def buscar_contacto(self):
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        encontrados = [contacto for contacto in self.contactos if nombre_buscar.lower() in contacto['nombre'].lower()]
        
        if encontrados:
            for contacto in encontrados:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
        else:
            print("No se encontró ningún contacto con ese nombre.")

    def editar_contacto(self):
        nombre_editar = input("Ingrese el nombre del contacto que desea editar: ")
        contacto_encontrado = None
        
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre_editar.lower():
                contacto_encontrado = contacto
                break
        
        if contacto_encontrado:
            print("Seleccione el dato a editar:")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. Email")
            opcion = input("Ingresa tu  opción: ")
            
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                contacto_encontrado['nombre'] = nuevo_nombre
            elif opcion == "2":
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                contacto_encontrado['telefono'] = nuevo_telefono
            elif opcion == "3":
                nuevo_email = input("Ingrese el nuevo email: ")
                contacto_encontrado['email'] = nuevo_email
            else:
                print("Opción no válida.")
            
            print("Contacto actualizado exitosamente.")
        else:
            print("No se encontró el contacto.")

    def cerrar_agenda(self):
        print("Cerrando agenda. ¡Hasta pronto!")
        exit()

def menu():
    agenda = Agenda()

    while True:
        print("\n--- Menú ---")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agenda.agregar_contacto()
        elif opcion == "2":
            agenda.listar_contactos()
        elif opcion == "3":
            agenda.buscar_contacto()
        elif opcion == "4":
            agenda.editar_contacto()
        elif opcion == "5":
            agenda.cerrar_agenda()
        else:
            print("lo sentimos Opción no válida. Por favor, intente nuevamente.")

menu()

