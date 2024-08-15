listacombinada=[]

def combinar_lista(lista1,lista2) :
   cantidad = len(lista1)
   if len(lista2)< cantidad:
       cantidad = len(lista2)

   for i in range(cantidad) :
        listacombinada.append(lista1[i])
        listacombinada.append(lista2[i])
   if len(lista1) > len(lista2):
      listacombinada.extend(lista1[cantidad:])
   else:
       listacombinada.extend(lista2[cantidad:])
   return listacombinada

lista1=["a","b","c"]
lista2=[1,2,3,4,5]
print(combinar_lista(lista1,lista2))


