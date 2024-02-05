# Serie Fibonacci
def serieFibo(n): 
        num = n
        a = 0
        b = 1
        print("0")
        print("1")
        for i in range (n-2):
            c = a + b
            a = b
            b = c 
            print(c)

# Jueguito Monedas
from random import randint

def jugar_adivina_numero():
    print("""
      Bienvenido!!! 
      El juego consiste en adivinar un número secreto del 1 al 100.
      Tienes 10 intentos para adivinar el número; de lo contrario, se cerrará el juego.
       """)

    numero_secreto = randint(1, 100)
    contar = 10
    intentos = 1

    while contar != 0:
        print("Intento #", intentos)
        print("Ingresa un número mayor o igual a 1 y menor o igual a 100")
        num = int(input())

        if intentos == 10:
            print("Lo lamento, no tienes más intentos.")
            break
        else:
            if num == numero_secreto:
                print("¡Felicidades! Has adivinado el número.")
                print("Adivinaste el número en", intentos, "intentos.")
                print("Fin del juego.")
                contar = 0
            elif num < numero_secreto:
                print("El número secreto es mayor al número ingresado.")
                contar -= 1
                intentos += 1
            elif num > numero_secreto:
                print("El número secreto es menor al número ingresado.")
                contar -= 1
                intentos += 1