
from random import randint

print("""
      Bienvenido!!! 
      El juego consiste en adivinar un número secreto del 1 al 100.
      Tienes 10 intentos para adivinar el número de lo contrario se cerrara el juego.
       """)

numeroSecreto = randint(1,100)
contar = 10
intentos = 1


while (contar != 0):
    print("Intento # ",intentos)
    print("Ingresa un número mayor o igual a 1 y menor o igual a 100")
    num = int(input())
    
    if intentos==10:
        print("Lo lamento, No tienes mas intentos")
        break
    else:
        if (num == numeroSecreto):
            print("Felicidades has adivinado el número.")
            print("Adivinaste el número en ",intentos, " intentos.")
            print("Fin del juego.")
            contar = 0
        elif (num < numeroSecreto):
            print("El número secreto es mayor al número ingresado.")
            contar -= 1
            intentos += 1
        elif (num > numeroSecreto):
            print("El número secreto es menor al número ingresado.")
            contar -= 1
            intentos+=1


#Desarrollado por: Kenia Yulieth Hernandez Diaz - 1098386069