print("Ingrese el año")
año=int(input())
if ((año%4==0) and (año%100!=0)) or (año%400==0) :
    bisiesto=True
else :
    bisiesto=False
print("Ingrese el mes")
mes=int(input())
print("Ingrese el dia")
dia=int(input())
if mes==2 and bisiesto==True :
    if dia>29 or dia<1 :
        print("Fecha no valida")
    else :
        print("La fecha es " ,dia,"/",mes,"/",año,)
if mes==2 and bisiesto==False :
    if dia>28 or dia<1 :
        print("Fecha no valida")
    else :
        print("La fecha es " ,dia,"/",mes,"/",año,)
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 :
    if dia>31 or dia<1 :
        print("Fecha no valida")
    else :
        print("La fecha es " ,dia,"/",mes,"/",año,)
if mes==4 or mes==6 or mes==9 or mes==11 :
    if dia>30 or dia<1 :
        print("Fecha no valida")
    else :
        print("La fecha es " ,dia,"/",mes,"/",año,)
if mes>12 or mes<1 :
    print("Fecha no valida")