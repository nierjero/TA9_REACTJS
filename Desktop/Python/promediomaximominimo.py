listanotas=[]
for i in range(5) :
    print("Ingrese una nota")
    nota=int(input())
    if nota < 0 or nota > 10 :
        print("Nota no valida")
    listanotas.append(nota)

promedio = 0

max = listanotas[0]
min = listanotas[0]

for num in listanotas:
    if num > max:
        max = num
    if num < min:
        min = num


promedio=sum(listanotas)/len(listanotas)


print(listanotas)
print("El promedio es ",int(promedio))
print("El minimo es ",min)
print("El máximo es ",max)