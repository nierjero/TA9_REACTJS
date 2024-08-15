lista_num_ingresados=[]
lista_num_comprimidos=[]
print("Ingrese un numero (Escribir -1 para terminar de ingresar)")
def comprimir_lista(lista_num_ingresados) :
 num=int(input())
 cantidad=0
 while num != -1 :
     valor=num
     for i in lista_num_ingresados :
         if i == valor :
          cantidad=cantidad+1 
         else :
             lista_num_comprimidos.append(valor)
             lista_num_comprimidos.append(cantidad)
             cantidad=0
     num=int(input())
 return lista_num_comprimidos
print(comprimir_lista(lista_num_comprimidos))

