def escribir_en_texto() :
    texto_usuario = str(input("Ingrese el texto que será grabado en el archivo "))
    nombre_archivo = str(input("Ingrese el nombre del archivo al cual grabar el texto "))
    while texto_usuario != "::q" :
         archivo_grabar = open(nombre_archivo,"a")
         archivo_grabar.write(texto_usuario)
         texto_usuario = str(input("Ingrese el texto que será grabado en el archivo "))
         if texto_usuario == "::q" :
            break
         nombre_archivo = str(input("Ingrese el nombre del archivo al cual grabar el texto "))
         archivo_grabar.write(texto_usuario)
    respuesta_ver =str(input("Quiere ver lo que grabó?(si/no) "))
    if respuesta_ver == "si" :
        mostrar_archivo = open(nombre_archivo,"r")
        for linea in mostrar_archivo :
            print(linea)
    else :
        print("Fin del grabado de texto")
escribir_en_texto()