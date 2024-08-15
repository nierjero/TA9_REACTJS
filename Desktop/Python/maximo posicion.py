lista_no_ordenada=[3,9,13,7]
def maximo_posición(lista_no_ordenada) :
    mayorposición=[]
    max=lista_no_ordenada[0]
    posición=0
    for valor in range(len(lista_no_ordenada)) :
        if lista_no_ordenada[valor] > max :
            max=lista_no_ordenada[valor]
            posición=valor
    mayorposición.append(max)
    mayorposición.append(posición)
    return mayorposición

print("El número de mayor valor y su posición:",maximo_posición(lista_no_ordenada))