multiplos7=[]
numeros_entre_a_y_b=[]
multiplos7_entre_ab=[]
x,a,b = int(input("Ingrese x ")),int(input("Ingrese a ")),int(input("Ingrese b "))
limite_x=b
multiplicador7=1
limite_a=b-a
numeros=a
while limite_x > 0 :
    multiplos=x*multiplicador7
    multiplos7.append(multiplos)
    multiplicador7=multiplicador7+1
    limite_x=limite_x-1
while limite_a > -1 :
    numeros_entre_a_y_b.append(numeros)
    numeros=numeros+1
    limite_a=limite_a-1
for multiplo in multiplos7 :
    if multiplo in numeros_entre_a_y_b :
        multiplos7_entre_ab.append(multiplo)
print("Multiplos ",multiplos7)
print("Numero entre a y b ",numeros_entre_a_y_b)
print("Multiplos de ",x,"Entre ",a,"y ",b," ",multiplos7_entre_ab)