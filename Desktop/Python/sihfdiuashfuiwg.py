def archivos_intercalados(archivo1, archivo2):
    archivo_mezclado = "Archivo_Mezclado.txt"
    leer_arch1 = open(archivo1, "r")
    leer_arch2 = open(archivo2, "r")
    agregar_archMz = open(archivo_mezclado, "a")

    lineas_arch1 = leer_arch1.readlines()
    lineas_arch2 = leer_arch2.readlines()

    num_lineas = max(len(lineas_arch1), len(lineas_arch2))

    for i in range(num_lineas):
        if i < len(lineas_arch1):
            agregar_archMz.write(lineas_arch1[i])
        if i < len(lineas_arch2):
            agregar_archMz.write(lineas_arch2[i])

    leer_arch1.close()
    leer_arch2.close()
    agregar_archMz.close()

    return archivo_mezclado


archivo1 = "ArchivoEjemplo1.txt"
archivo2 = "ArchivoEjemplo2.txt"
archivos_intercalados(archivo1, archivo2)
