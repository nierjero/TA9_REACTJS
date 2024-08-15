import random 
lista=[]
for i in range(10):
    lista.append(random.randint(1,10))
print (lista)

def cuadradocubo(lista) :
    for i in(lista) :
        cuadrado= i**2
        cubo=i**3
        print(i, "cuadrado = ",cuadrado)
        print(i, "cubo =", cubo)

resultado=cuadradocubo(lista)