listanombreseparados=[["Solid","Snake"],["Big","Boss"]]
def juntarnombres (listanombreseparados) :
    listanombreunidos=[]
    for i in listanombreseparados :
        listanombreunidos.append(" ".join(i))
    return listanombreunidos

print(juntarnombres(listanombreseparados))