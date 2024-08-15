import random

def loteria() :
 fila1=[]
 fila2=[]
 fila3=[]
 cartonloteria=[]
 while len(fila1) < 5 :
     numfila1=random.randint(1,99)
     if numfila1 not in fila1 :
         fila1.append(numfila1)
 while len(fila2) < 5 :
     numfila2=random.randint(1,99)
     if numfila2 not in fila2 and numfila2 not in fila1 :
         fila2.append(numfila2)
 while len(fila3) < 5 :
     numfila3=random.randint(1,99)
     if numfila3 not in fila1 and numfila3 not in fila2 and numfila3 not in fila3 :
         fila3.append(numfila3)
 cartonloteria.append(fila1)
 cartonloteria.append(fila2)
 cartonloteria.append(fila3)
 print(cartonloteria)

loteria()