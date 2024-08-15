import math
def desviación_estándar() :
    valor=float(input("Ingrese un valor "))
    contador_promedio=0
    sumatoria=0
    sumacuadrados=0
    while valor != -1 :
        sumatoria=sumatoria+valor
        contador_promedio=contador_promedio+1
        sumacuadrados=sumacuadrados+(valor**2)
        valor=float(input("Ingrese un valor "))
    promedio=sumatoria/contador_promedio
    desviación_estándarr=(sumacuadrados/contador_promedio)-(promedio**2)
    desviación_estándarr=math.sqrt(desviación_estándarr)
    return desviación_estándarr

print(desviación_estándar())