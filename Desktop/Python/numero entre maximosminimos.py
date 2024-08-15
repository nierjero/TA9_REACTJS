min=10
max=50
def obtener_entero(mensaje, min, max) :
    while mensaje < min or mensaje > max :
        mensaje=int(input("Valor invalido, vuelva a ingresar un valor entre 10 y 50 "))
    else :
        print("El valor es ",mensaje)

mensaje=int(input("Ingrese un valor "))
obtener_entero(mensaje,min,max)