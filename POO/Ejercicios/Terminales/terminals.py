"""
Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos
a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa
principal que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que
validarse como tales al crear el objeto (solo dígitos, empiezan por 9, 6 o 7, su longitud es de nueve dígitos) y no
puede haber dos terminales con el mismo número.

Autor: Ángel Ortiz Torres
"""
from __future__ import annotations
from typeguard import typechecked

@typechecked
class Terminal:
    NAME_FILE = 'terminals.txt'

    def __init__(self, phone_number: str):
        if len(phone_number) != 9:
            raise ValueError("Longitud del número de teléfono incorrecto")
        if phone_number[0] not in ['6', '7', '9'] or not phone_number.isdigit():
            raise ValueError("Los números de teléfono no válido")

        try:
            with open(self.__class__.NAME_FILE, 'rt') as file:
                existing_numbers = file.read().splitlines()
                if phone_number in existing_numbers:
                    raise ValueError("El número de teléfono ya existe")
        except FileNotFoundError:
            pass

        with open(self.__class__.NAME_FILE, 'at') as file:
            file.write(phone_number + '\n')

        self.__phone_number = phone_number
        self.__time = 0

    def number(self, other: Terminal):
        if self.__phone_number == other.__phone_number:
            raise ValueError("No pueden haber dos terminales con el mismo número")

    @property
    def phone_number(self):
        return self.__phone_number

    def call(self, phone: Terminal, time: int):
        if time < 0:
            raise ValueError("El tiempo no puede ser negativo")
        if self.__phone_number == phone.__phone_number:
            raise ValueError("Un número no puede llamarse a sí mismo")
        self.__time += time
        phone.__time += time

    def __str__(self):
        return f"Nº {self.__phone_number} - {self.__time}s de conversación"