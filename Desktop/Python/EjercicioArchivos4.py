def numero_lineas_string(string) :
    contador_lineas = 0
    contenido_archivo = open("Archivo_Mezclado.txt","r")
    for lineas in contenido_archivo :
        contador_lineas += 1 
        if string in lineas :
            print(string, "esta en la línea", contador_lineas)
string = "locura"
numero_lineas_string(string)