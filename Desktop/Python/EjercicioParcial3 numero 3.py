def productos_comunes(inventario1, inventario2):
    inventarios_juntos = {}
    for stock in inventario1 :
        if stock in inventario2 : 
            inventarios_juntos[stock] = (inventario1.get(stock)) + (inventario2.get(stock)) 
    return inventarios_juntos
inventario1 = {"Manzanas" : 10, "Peras" : 15, "Bananas" : 30}
inventario2 = { "Peras" : 15, "Bananas" : 30}
print(productos_comunes(inventario1, inventario2))