"""
Este programa muestra un gestor de vehículos en el que posteriormente se verán diferentes funciones mediante un menú.

Autor: Ángel Ortiz Torres
"""
from abc import ABC

class Vehicle(ABC):
    __vehicles_created = 0
    __total_kilometers = 0

    def __init__(self):
        self.__kilometers_traveled = 0
        Vehicle.__vehicles_created += 1

    def travel(self, kilometer):
        self.__kilometers_traveled += kilometer
        Vehicle.__total_kilometers += kilometer

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

class Bike(Vehicle):

    @classmethod
    def do_wheelie(cls):
        print("¡Has hecho un caballito con la bicicleta!")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel = 0.0

    def travel(self, kilometer):
        max_possible_km = self.fuel / 0.1
        km_to_travel = min(kilometer, max_possible_km)

        if km_to_travel < kilometer:
            raise ValueError("No hay suficiente combustible. Solo se han recorrido", round(km_to_travel, 2), "kilometer.")

        self.fuel -= km_to_travel * 0.1
        super().travel(km_to_travel)

    def burn_rubber(self):
        if self.fuel >= 1:
            self.fuel -= 1
            print("¡Quemando rueda!")
        else:
            raise ValueError("No hay suficiente combustible para quemar rueda.")

    def fill_tank(self):
        self.fuel = 50.0

