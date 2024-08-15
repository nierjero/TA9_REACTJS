#Conjuntos
#crear conjuntos: literal y con set
#literal
A= {2,3,4}
B={2,5,6}
#set
conjunto_set= set([6,3,6,9])
#para agregar un elemento
conjunto_set.add('rojo')
#agregar muchos elementos
conjunto_set.update({'violeta', 'azul'})

union= A | B
interseccion= A & B
#para eliminar
union.discard(4)
#para ver la diferencia entre conjuntos
diferencia=A-B
#para ver la diferencia simetrica entre conjuntos
diferencia_simetrica= A^B
#para devolver un elemento que eliminamos
union.pop()
#para ver si A y B son congruentes o amplios (devuelve True o False) < o > amplio y <= o >= congruentes (estrictos)
print(A<B)
print(A<=B)
#Para usar el in (devuelve True o False):
if 4 in A:
    print ('4 está en A virgo')
#Para usar len (cantidad de elementos del conjunto)
print(len(A))