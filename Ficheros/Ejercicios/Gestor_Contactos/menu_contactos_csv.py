"""
El objetivo del ejercicio es crear un programa en Python que gestione un archivo CSV llamado contactos.csv usando
el módulo csv y control de excepciones. El programa debe permitir:

1. Crear el archivo CSV con cabecera si no existe.

2. Mostrar los contactos guardados.

3. Añadir nuevos contactos, evitando duplicados.

4. Buscar un contacto por nombre.

5. Eliminar un contacto por nombre.

Además, se deben manejar errores como archivos inexistentes o problemas al escribir/leer usando try/except,
mostrando siempre mensajes adecuados.

Autor: Ángel Ortiz Torres
"""
from contactos_csv import Contact
from menu import Menu

NAME_FILE_CONTACTS = "Ficheros/Ejercicios/Gestor_Contactos/contactos.csv"

contacts = Contact(NAME_FILE_CONTACTS)

menu = Menu("Crear archivo", "Mostrar contactos", "Añadir contacto", "Buscar contacto por nombre",
            "Eliminar contacto por nombre", "Salir", title="Gestor de Contactos")

while True:
    user_option = menu.choose()

    match user_option:
        case 1:
            if contacts.create_file():
                print("El archivo ha sido creado correctamente.\n")
            else:
                print("El archivo ya existe.\n")
        case 2:
            show = contacts.show_contacts()
            print(show)
        case 3:
            user_name = input("Nombre: ")
            user_phone = int(input("Teléfono: "))
            user_email = input("Correo: ")
            add_contact = contacts.add_contact(user_name, user_phone, user_email)
            print(add_contact)
        case 4:
            name = input("¿Qué contacto quieres buscar? ")
            search = contacts.search_contact_by_name(name)
            print(search)
        case 5:
            name = input("¿Qué contacto quieres borrar? ")
            delete = contacts.delete_contact_by_name(name)
            print(delete)
        case 6:
            print("¡Nos vemos en la próxima!")
            exit()
