def contar_str_archivo(archivo,string) :
    f=open(archivo,"r")
    contador_raretes = 0
    contador_lineas = 0
    print(f)
    for linea in f :
      contador_lineas += 1
      if string in linea :
        contador_raretes += 1 
    print(contador_raretes)
    print(contador_lineas)

    f.close()

archivo = "ArchivoEjemplo1.txt"
string = "rarete no?"
contar_str_archivo(archivo,string)