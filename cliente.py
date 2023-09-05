from cliente import Cliente  

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
