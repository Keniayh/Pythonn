def funciondia1():
    ##------------------------------------------------------------------------------
    ##--------------------------------Ejercicio-------------------------------------
    ##------------------------------------------------------------------------------

    #Impresion en consola
    print("Hola, mundo")

    #Datos primitivos
    # 1. String
    texto = "campus"
    print(texto)
    print(type(texto))

    # 2. INT
    numeroEntero = 3
    print(numeroEntero)
    print(type(numeroEntero))

    # 3. Float
    numeroDecimal = 3.1
    print(numeroDecimal)
    print(type(numeroDecimal))

    # 4. Double
    numeroDecimalLargo = 3.14167621635615371123456789
    print(numeroDecimalLargo)
    print(type(numeroDecimalLargo))

    # 5. Bolean
    boleano = True
    print(boleano)
    print(type(boleano))

    #---- Entradas parte del usuario----
    entradaUsuarioNumero = input("Ingresa tu nombre: ")
    print("Tu nombre es: ", entradaUsuarioNumero)

    #---- Entradas parte del usuario con definición de tipo de dato primitivo ----
    entradaUsuarioNumero = int(input("Ingresa tu edad: "))
    print("Tu edad es: ", entradaUsuarioNumero)

    # Otra forma
    numeroFinal = int(entradaUsuarioNumero)
    print(numeroFinal)

    #---- Ciclos ----
    #Ciclo FOR
    for i in range(5):
        print(i)

    #Ciclo FOR 2.0
    for i in range (5,10,2): #for 'contador' in range (desde,hasta,pasos):
        print(i)

    #Ciclo WHILE
    booleanito = True
    while booleanito == True: #while 'condicion_a_cumplir':
        print("Sigo vivo")
        booleanito = False

    #---- Condicionales ----
    texto1 = "Campus"
    if texto1 == "Campus":
        print("Soy campus")
    else:
        print("No soy campus.")

    #---- Array -----
    # 1. Lista

    nombres = list(["Sofia", "Maicol", "Juan Diego", "Matias"])
    print(nombres[2])

    #---- Funciones-----

    # 1. Con parametros y con retorno

    def areaCuadrado(k):
        lado = k
        areaTotal = k*k
        return "El area del cuadrado es: ", float((areaTotal))

    lado = input("Ingresa el lado del cuadrado: ")

    print(areaCuadrado(int(lado)))

    # 2. Sin parametros y con retorno

    def nombre():
        name = "Matias"
        return "Su nombre es: ", name

    print (nombre())

    # 3: Con parametros y sin retorno

    def division(a,b):
        num1 = a
        num2 = b
        divi = a/b
        print("El resultado de la división es: ", float((divi)))

    division(25,5)

    # 4. Sin parametros y sin retorno

    def numeros():
        n  = 1
        n1 = 2
        n2 = 3
        n3 = 4
        n4 = 5
        print("Numeros del 1 al 5: ", n, n1, n2, n3, n4)

    numeros()

