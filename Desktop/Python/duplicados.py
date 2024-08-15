listanorepetidos=[]
listarepetidos=[1,1,1,2,2,2,3,3,3]
def eliminarrepetidos(listarepetidos) :
    for i in listarepetidos :
        if i not in listanorepetidos :
            listanorepetidos.append(i)
    return listanorepetidos
resultado=eliminarrepetidos(listarepetidos)
print(resultado)