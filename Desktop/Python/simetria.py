lista1=[1,2,3,4]
lista2=[3,4,5,6]
listasimetrica=[]
listanosimetrica=lista1+lista2 
for i in listanosimetrica :
    if i in lista1 and i not in lista2 :
        listasimetrica.append(i)
    elif i not in lista1 and i in lista2 :
        listasimetrica.append(i)

print(listasimetrica)

