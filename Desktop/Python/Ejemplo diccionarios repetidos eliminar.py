def eliminar_repetidos(diccionario):
    diccionario_aux = {}

    for clave, lista in diccionario.items():
        lista_sin_repetidos = []

        for elemento in lista:
            if elemento not in diccionario_aux.values():
                lista_sin_repetidos.append(elemento)
                diccionario_aux[clave] = lista_sin_repetidos

    return diccionario_aux


diccionario_original = {
    "clave1": [1, 2, 3, 4],
    "clave2": [2, 4, 6, 8],
    "clave3": [3, 6, 9, 12],
    "clave4": [4, 8, 12, 16]
}

diccionario_sin_repetidos = eliminar_repetidos(diccionario_original)
print(diccionario_sin_repetidos)
