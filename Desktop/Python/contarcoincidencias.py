lista_desordenada=[1,1,4,7,7,7,9,0,0,6,6]
elemento=7
def coincidencias(lista_desordenada,elemento) :
    contador=0
    for valor in lista_desordenada :
        if valor==elemento :
            contador+=1
    return contador

print("La cantidad de coincidencias es de",coincidencias(lista_desordenada,elemento))

lista_desordenada=[1,1,4,7,7,7,9,0,0,6,6]
elemento=7
def coincidenciasposicion(lista_desordenada,elemento) :
    for valor in range(len(lista_desordenada)) :
        if lista_desordenada[valor]==elemento :
            posición=valor
            break
    return posición

print("La posición de la primera coincidencia es",coincidenciasposicion(lista_desordenada,elemento))

lista_desordenada_solo=[1,1,4,7,7,7,9,0,0,6,6]
lista_cantidad_posición=[]
elemento_solo=7
cantidad=coincidencias(lista_desordenada,elemento)
posición=coincidenciasposicion(lista_desordenada,elemento)
lista_cantidad_posición.append(cantidad)
lista_cantidad_posición.append(posición)
print("La cantidad de coincidencias, y la posicion de la primera concidencia es de",lista_cantidad_posición)