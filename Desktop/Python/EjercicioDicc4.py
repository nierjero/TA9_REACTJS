dicc = {}
nombre=str(input("Ingrese un nombre "))
while nombre != "" :
  if nombre in dicc :
     dicc[nombre]+= 1
  else :
     dicc[nombre]=1
  nombre=str(input("Ingrese un nombre "))
print(dicc)
