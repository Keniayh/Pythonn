comidaGato = dict
comidaGato = {'Mirringo': 7000, 'Q-ida cat': 4500, 'Cat Chow': 8500}
total = 0

def gatos():
    fin = 1
    while fin != 0:
        print("""
              Bienvenido a la tienda 'Siempre Michis',
              por el momento solo tenemos 3 productos a la venta:
              'Mirringo', 'Q-ida cat', 'Cat Chow'""")
        producto = input("Ingresa el producto que deseas: ")
        comida = comidaGato.get(producto, "Producto no encontrado")
        
        if comida != "Producto no encontrado":
            print(f"El producto '{producto}' se encuentra y su precio es: {comida}")
            print("¿Deseas comprar el producto?")
            x = input("1 = sí, 2 = no: ")
            
            if x == "1":
                print("¡Comprado!")
                global total
                total += comida
            elif x == "2":
                print("¿Quieres buscar otro producto?")
                a = input("1 = sí, 2 = no: ")
                if a == "1":
                    print("Continúa viendo otros productos.")
                else:
                    print("El total a pagar es de: ", total)
                    fin = 0
        else:
            print("Producto no encontrado. ¿Quieres buscar otro producto?")
            a = input("1 = sí, 2 = no: ")
            if a == "1":
                print("Continúa viendo otros productos.")
            else:
                print("El total a pagar es de: ", total)
                fin = 0

gatos()
