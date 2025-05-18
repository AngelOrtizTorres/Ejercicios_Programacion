from save_movements import BankAccount

NAME_FILE = "Ficheros/Ejercicios/Guardar_Movimientos_Cuenta_Bancaria/save_account.txt"

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

print(cuenta2.movements())

cuenta2.save_to_file(NAME_FILE)
print("\nCuenta2 guardada.")

cuenta_cargada = BankAccount.from_file(NAME_FILE)
print("\nCuenta cargada desde fichero:")
print(cuenta_cargada)
print(cuenta_cargada.movements())