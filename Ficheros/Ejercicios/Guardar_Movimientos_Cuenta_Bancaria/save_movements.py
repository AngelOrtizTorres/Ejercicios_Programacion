"""
Ampliar ejercicio sobre Cuentas Bancarias añadiendo un sistema de movimientos

Autor: Ángel Ortiz Torres
"""
from __future__ import annotations
from typeguard import typechecked
import random

@typechecked
class BankAccount:
    NAME_FILE_BANK_ACCOUNT = "POO/Ejercicios/Cuenta_Bancaria/accounts.txt"

    def __init__(self, money: float = 0):
        if money < 0:
            raise ValueError("El saldo no puede ser negativo")

        number_account = f"{random.randint(0, 9999999999):010}"

        try:
            with open(self.__class__.NAME_FILE_BANK_ACCOUNT, 'rt') as file:
                existing_accounts = file.readlines()
                if number_account in existing_accounts:
                    raise ValueError("El número de teléfono ya existe en el archivo")
        except FileNotFoundError:
            pass

        with open(self.__class__.NAME_FILE_BANK_ACCOUNT, 'at') as file:
            file.write(str(number_account) + '\n')

        self.__money = money
        self.__number = number_account
        self.__history = []

    @property
    def money(self):
        return self.__money

    @property
    def number(self):
        return self.__number

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("No puedes depositar dinero negativo")
        self.__money += amount
        self.__history.append(f"Ingreso de {amount} € Saldo: {self.__money:.2f} €")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("No puedes retirar dinero negativo")
        if self.__money - amount < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__money -= amount
        self.__history.append(f"Cargo de {amount} € Saldo: {self.__money:.2f} €")

    def transfer(self, account: BankAccount, amount: float):
        self.__check_transfer(account, amount)
        self.__money -= amount
        account.__money += amount

    def __check_transfer(self, account: BankAccount, amount: float):
        if self.__money == account.__money:
            raise ValueError("No puedes transferir dinero a la misma cuenta")
        if amount <= 0: 
            raise ValueError("No puedes transferir dinero negativo")
        if self.__money - amount < 0:
            raise ValueError("El saldo restante no puede ser negativo")
        self.__history.append(f"Transferencia emitida de {amount} € a la cuenta {account.number} Saldo: {self.__money:.2f} €")
        account.__history.append(f"Transferencia recibida de {amount} € de la cuenta {self.number} Saldo: {account.money:.2f} €")

    def movements(self):
        header = f"Movimientos de la cuenta {self.__number}\n" + "-" * 35
        return header + "\n" + "\n".join(self.__history)
    
    def save_to_file(self, filename: str):
        try:
            with open(filename, 'w') as f:
                f.write(f"{self.__number}\n")
                f.write(f"{self.__money}\n")
                for movement in self.__history:
                    f.write(movement + "\n")
            print(f"Cuenta guardada correctamente en {filename}")
        except FileNotFoundError:
            print("Error al guardar en fichero")

    @classmethod
    def from_file(cls, filename: str) -> BankAccount:
        try:
            with open(filename, 'r') as f:
                lines = f.read().splitlines()
                number = lines[0]
                balance = float(lines[1])
                history = lines[2:]
                return cls(money=balance, number=number, history=history)
        except FileNotFoundError:
            print("El archivo no existe.")
            raise

    def __str__(self):
        return f"Número de cta: {self.__number}  Saldo: {self.__money:.2f} €"