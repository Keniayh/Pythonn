tex = 1
while tex == 1:
    print("""Bienvenido!
        
    A continuación ingresaras un número para determinar hasta que termino de la secuencia deseas generar.
        
    La serie de Fibonacci es, en matemáticas, una secuencia ordenada de números descrita por Leonardo de Pisa, 
    matemático italiano del siglo XIII""")
 
    num = int(input("Ingresa un número mayor a 1 para determinar hasta que termino de la secuencia deseas generar: "))
    if num == 1:
        print("0")
        break

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
 
    serieFibo(int(num))

    print("Desea seguir explorando la serie de Fibonacci?, tenga en cuenta que 1 = si y 0 = no.")
    texto = input()
    
    if texto == "0":
        tex = 0
    else:
        tex = 1


#Desarrollado por: Kenia Yulieth Hernandez Diaz - 1098386069