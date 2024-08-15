def archivos_intercalados(archivo1,archivo2) :
    archivo_mezclado = "Archivo_Mezclado.txt"
    leer_arch1 = open(archivo1,"r")
    leer_arch2 = open(archivo2,"r")
    agregar_archMz = open(archivo_mezclado,"a")

    lineas_archivo1 = leer_arch1.readlines()
    lineas_archivo2 = leer_arch2.readlines()

    if len(lineas_archivo1) > len(lineas_archivo2) :
        limite = len(lineas_archivo1)
    elif len(lineas_archivo2) > len(lineas_archivo1) :
        limite = len(lineas_archivo2)
    else :
        limite = len(lineas_archivo1)
    for i in range(limite) :
      if i < len(lineas_archivo2) :  
        agregar_archMz.write(lineas_archivo2[i])
      if i < len(lineas_archivo1) :
        agregar_archMz.write(lineas_archivo1[i])
    return archivo_mezclado

archivo1 = "ArchivoEjemplo1.txt"
archivo2 = "ArchivoEjemplo2.txt"
archivos_intercalados(archivo1,archivo2) 