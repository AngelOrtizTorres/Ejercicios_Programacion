from __future__ import annotations
from typeguard import typechecked
from Terminales.terminals import Terminal

@typechecked
class Mobile(Terminal):
    __tariffs = {
        "rata": 0.06,
        "mono": 0.12,
        "bisonte": 0.30
    }

    def __init__(self, phone_number: str, tariff: str):
        if tariff not in Mobile.__tariffs:
            raise ValueError("Tarifa incorrecta. Debe ser 'rata', 'mono' o 'bisonte'")
        super().__init__(phone_number)
        self.__tariff = tariff
        self.__cost = 0.0

    def call(self, phone: Terminal, time: int):
        super().call(phone, time)

        cost_per_minutes = Mobile.__tariffs[self.__tariff] / 60
        self.__cost += time * cost_per_minutes

    def change_tariff(self, new_tariff: str):
        if new_tariff not in Mobile.__tariffs:
            raise ValueError("Tarifa incorrecta. Debe ser 'rata', 'mono' o 'bisonte'")
        self.__tariff = new_tariff

    def __str__(self):
        formatted_number = f"{self.phone_number[:3]} {self.phone_number[3:5]} {self.phone_number[5:7]} {self.phone_number[7:]}"
        return f"Nº {formatted_number} - {self._Terminal__time}s de conversación - tarificados {self.__cost:.2f} euros"
