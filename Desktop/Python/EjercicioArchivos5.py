def concatenar_archivos(lista_archivos) :
    archivo_nexo = "Archivo_nexo.txt"
    archivo_nexo_agregar = open(archivo_nexo,"a")
    for archivo in lista_archivos :
        contenido_archivo = open(archivo,"r")
        for lineas in contenido_archivo :
            linea_abajo = lineas.rstrip()
            archivo_nexo_agregar.write(linea_abajo + "\n")
    return archivo_nexo

lista_archivos = ["ArchivoEj5_1.txt","ArchivoEj5_2.txt","ArchivoEj5_3.txt"]
concatenar_archivos(lista_archivos)