from vehicle import *

bike = Bike()
car = Car()

def mostrar_menu():
    print("""
VEHÍCULOS
=========
1. Anda con la bicicleta.
2. Haz el caballito con la bicicleta.
3. Anda con el coche.
4. Quema rueda con el coche.
5. Llena el depósito del coche.
6. Ver kilometraje de la bicicleta.
7. Ver kilometraje del coche.
8. Ver el combustible que queda en el depósito del coche.
9. Ver kilometraje total.
10. Salir.
""")

while True:
    mostrar_menu()
    option = input("Elige una opción (1-10): ")

    match option:
        case "1":
            km = float(input("¿Cuántos kilómetros quieres recorrer con la bicicleta? "))
            bike.travel(km)
        case "2":
            bike.do_wheelie()
        case "3":
            km = float(input("¿Cuántos kilómetros quieres recorrer con el coche? "))
            car.travel(km)
        case "4":
            car.burn_rubber()
        case "5":
            car.fill_tank()
            print("Depósito lleno. 50 litros disponibles.")
        case "6":
            print(f"Kilometraje de la bicicleta: {bike.kilometers_traveled} kilómetros")
        case "7":
            print(f"Kilometraje del coche: {car.kilometers_traveled} kilómetros")
        case "8":
            print(f"Combustible restante en el coche: {round(car.fuel, 2)} litros")
        case "9":
            print(f"Kilometraje total: {Vehicle.total_kilometers} kilómetros")
        case "10":
            print("¡Hasta la próxima!")
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
