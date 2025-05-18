"""
Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta
se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número de
cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente.
En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra.
No se permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de este, en el que se
pide llevar un registro de los movimientos realizados.

Autor: Ángel Ortiz Torres
1/4/2025
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

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("No puedes retirar dinero negativo")
        if self.__money - amount < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__money -= amount

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

    def __str__(self):
        return f"Número de cta: {self.__number}  Saldo: {self.__money:.2f} €"
    
if __name__ == "__main__":
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
