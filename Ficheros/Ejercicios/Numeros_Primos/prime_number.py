"""
Programa que guarda en un fichero los números primos del 1 al 500
"""

NAME_FILE_NUMBERS = "Ficheros/Ejercicios/Numeros_Primos/primes_numbers.txt"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    with open(NAME_FILE_NUMBERS, "wt") as f:
        for i in range(1, 501):
            if is_prime(i):
                f.write(f"{i}\n")
    print("Números primos guardados correctamente")
except FileNotFoundError:
    print("Error al escribir en el fichero")