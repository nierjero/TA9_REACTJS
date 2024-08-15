class Carrito:
    def __init__(self,usuario):
        self.usuario = usuario
        self.productos = {}

    #Agrega un producto y su cantidad
    def agregar(self,producto,cantidad):
        self.productos[producto] =  cantidad

    #Obtiene la cantidad total de productos
    def cantidad_total(self):
        cantidad = 0
        for clave in self.productos:
            cantidad+=self.productos[clave]
        return cantidad
    
    def __str__(self):
        return f'Usuario: {self.usuario}'

    #Vacía el carrito
    def vaciar(self):
        self.productos = {}

    #Obtiene el monto a pagar
    def total_a_pagar(self):
        total = 0
        for clave in self.productos:
            total+=self.productos[clave]*clave.precio
        return total

   #permite verifica si el carrito está vacío
    def esta_vacio(self):
        return len(self.productos) == 0
          
class Juguete:
    def __init__(self, nombre, precio):
        self.nombre_juguete = nombre
        self.precio = precio

class Ropa:
    def __init__(self, tipo, color, precio):
        self.tipo = tipo 
        self.color = color
        self.precio = precio

mi_carrito = Carrito("Raiden")
Ropa1 = Ropa("Vans","Negro",2500)
Jugete1 = Juguete("Katana de goma",1000)
Jugete2 = Juguete("Lego de Batman",4500)
mi_carrito.agregar(Ropa1,2)
mi_carrito.agregar(Jugete1,2)
mi_carrito.agregar(Jugete2,1)
print(f"la cantidad total de objetos en el carrito es de {mi_carrito.cantidad_total()} objetos")
print(f"El monto a pagar por el carrito es de ${mi_carrito.total_a_pagar()}")
mi_carrito.vaciar()
print(f"¿El carrito esta vacio? :{mi_carrito.esta_vacio()}")