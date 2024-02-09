import json

# Función para agregar un nuevo cliente
def agregar_cliente(cliente):
    datos_ventas["ventas"]["clientes"].append(cliente)

# Función para actualizar información de un cliente por su ID
def actualizar_cliente(id_cliente, nueva_informacion):
    for cliente in datos_ventas["ventas"]["clientes"]:
        if cliente["id"] == id_cliente:
            cliente.update(nueva_informacion)
            break

# Función para eliminar un cliente por su ID
def eliminar_cliente(id_cliente):
    datos_ventas["ventas"]["clientes"] = [cliente for cliente in datos_ventas["ventas"]["clientes"] if cliente["id"] != id_cliente]

# Ejemplo de uso
nuevo_cliente = {"id": 11, "nombre": "Nuevo", "apellido1": "Cliente", "ciudad": "Barcelona", "categoría": 150}
agregar_cliente(nuevo_cliente)

print("Clientes después de agregar:")
print(datos_ventas["ventas"]["clientes"])

id_cliente_a_actualizar = 4
nueva_informacion_cliente = {"nombre": "NuevoNombre", "ciudad": "NuevaCiudad"}
actualizar_cliente(id_cliente_a_actualizar, nueva_informacion_cliente)

print("\nClientes después de actualizar:")
print(datos_ventas["ventas"]["clientes"])

id_cliente_a_eliminar = 5
eliminar_cliente(id_cliente_a_eliminar)

print("\nClientes después de eliminar:")
print(datos_ventas["ventas"]["clientes"])