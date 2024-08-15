listacartesiana=[]

def cartesiano(listaA,listaB) :
    for ea in listaA :
        for eb in listaB:
            listacartesiana.append([ea, eb])
    return listacartesiana

listaA=["a","b"]
listaB=[1,2,3]


print(cartesiano(listaA,listaB))


