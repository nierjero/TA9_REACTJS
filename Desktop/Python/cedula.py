def calcularverificador(ci) :

    multiplicadores=[2,9,8,7,6,3,4]
    suma=0
    for i in range(len(ci)):
        suma = suma + (int(ci[i]) * multiplicadores[i])
    resto=suma%10
    if resto == 0 :
        verificador=0
    else : 
        verificador=10-resto
    return verificador
    
ci="5435469"
print(calcularverificador(ci))

def verificacióncedula(cedula) :
    cedula = list(cedula)
    x= cedula.pop(-1)
    verificadorIngresado = x
    ci = cedula
    verificador = calcularverificador (ci)
    print(verificador)
    if int(verificadorIngresado) == verificador :
        Valido=True
    else:
        Valido=False
    return Valido

cedula="54354697"

print(verificacióncedula(cedula))