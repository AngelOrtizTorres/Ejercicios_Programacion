"""
Módulo para crear la clase Contact

Autor: Ángel Ortiz Torres
"""
import os
import csv
from typeguard import typechecked


@typechecked
class Contact:

    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def create_file(self):
        if os.path.exists(self.filename):
            self.initialize_file()
            return False
        else:
            self.initialize_file()
            return True

    def initialize_file(self):
        with open(self.filename, 'wt', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Teléfono', 'Correo electrónico'])

    def read_file(self):
        with open(self.filename, encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)
            contacts = list(reader)

        return contacts

    def show_contacts(self):
        try:
            if not os.path.exists(self.filename):
                return "El archivo no se encuentra.\n"

            contacts_info = []
            with open(self.filename, encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if row:
                        if len(row) == 3:
                            name, phone, email = row
                            contacts_info.append(f"Nombre: {name} | Teléfono: {phone} | Correo: {email}")

            if contacts_info:
                return "\n".join(contacts_info)
            else:
                return "No hay contactos para mostrar.\n"

        except FileNotFoundError:
            return "No se ha encontrado el contacto.\n"

    def add_contact(self, name: str, phone: int, email: str):
        if os.path.exists(self.filename):
            contacts = self.read_file()

            for row in contacts:
                if len(row) >= 3:
                    new_name, _, new_email = row
                    if new_name == name and new_email == email:
                        return "El contacto ya existe.\n"

        with open(self.filename, 'at', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])
            return "Contacto añadido correctamente.\n"

    def search_contact_by_name(self, name: str):
        try:
            if os.path.exists(self.filename):
                contacts = self.read_file()

            for row in contacts:
                if len(row) == 3:
                    contact_name, phone, email = row
                    if contact_name.lower() == name.lower():
                        return f"Contacto encontrado: Nombre: {contact_name} | Teléfono: {phone} | Correo: {email}\n"
        except FileNotFoundError:
            return "No se ha encontrado el contacto.\n"

    def delete_contact_by_name(self, name: str):
        try:
            if os.path.exists(self.filename):
                contacts = self.read_file()

                deleted = False
                updated_contacts = []

                for row in contacts:
                    if len(row) >= 1:
                        contact_name = row[0].strip().lower()
                        if contact_name == name.strip().lower():
                            deleted = True
                        else:
                            updated_contacts.append(row)

                if deleted:
                    with open(self.filename, 'wt', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(['Nombre', 'Teléfono', 'Correo electrónico'])
                        writer.writerows(updated_contacts)
                    return f"El contacto '{name}' ha sido eliminado correctamente.\n"
                else:
                    return f"No se ha encontrado un contacto con el nombre '{name}'.\n"
        except FileNotFoundError:
            return [f"Archivo no encontrado: {self.filename}"]

