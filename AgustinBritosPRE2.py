


class Cliente:
    def __init__(self, nombre, correo, direccion):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.carrito_compras = []

    def agregar_producto(self, producto):
        self.carrito_compras.append(producto)
        print(f"{producto} ha sido agregado a tu carrito de compras.")

    def eliminar_producto(self, producto):
        if producto in self.carrito_compras:
            self.carrito_compras.remove(producto)
            print(f"{producto} ha sido eliminado de tu carrito de compras.")
        else:
            print(f"{producto} no se encuentra en tu carrito de compras.")

    def ver_carrito(self):
        print("Tu carrito de compras contiene los siguientes productos:")
        for producto in self.carrito_compras:
            print(producto)

    def realizar_compra(self):
        if len(self.carrito_compras) > 0:
            total = sum([precio for precio in self.carrito_compras])
            print(f"Has realizado una compra por un total de ${total}. Gracias por tu compra.")
            self.carrito_compras = []
        else:
            print("Tu carrito de compras está vacío. Agrega productos antes de realizar una compra.")

# Clase para representar juegos de Nintendo
class JuegoNintendo:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    def __str__(self):
        return f"{self.titulo} - ${self.precio}"

# Ejemplo de uso
cliente1 = Cliente("Juan Perez", "juan@example.com", "Calle 123")

juego1 = JuegoNintendo("Super Mario Odyssey", 49.99)
juego2 = JuegoNintendo("The Legend of Zelda: Breath of the Wild", 59.99)

cliente1.agregar_producto(juego1)  # Agregar un juego de Nintendo al carrito
cliente1.agregar_producto(juego2)  # Agregar otro juego de Nintendo al carrito
cliente1.ver_carrito()  # Mostrar los juegos en el carrito
cliente1.realizar_compra()  # Realizar la compra
cliente1.ver_carrito()  # Ver carrito después de la compra
