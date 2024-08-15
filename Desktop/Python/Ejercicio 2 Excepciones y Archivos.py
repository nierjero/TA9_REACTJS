def ejercicio2arch() :
    try :
        sumatoria = 0
        contador = 0
        nombre_archivo = str(input("Ingrese el archivo a abrir"))
        contenido_archivo = open(nombre_archivo,"r")
        for linea in contenido_archivo :
            contador += 1 
            sumatoria += linea
        promedio = sumatoria/contador
        return promedio
    except FileNotFoundError :
        print("El archivo no se ha encontrado o no existe")

ejercicio2arch()