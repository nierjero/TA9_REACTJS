def vacunacion(lista_dep_vacunas) :
    try :
        dicc_vacunas_totales = {}
        for dias in lista_dep_vacunas :
            for departamento in dias :
                if departamento not in dicc_vacunas_totales :
                    dicc_vacunas_totales[departamento] = dias.get(departamento)
                else :
                    dicc_vacunas_totales[departamento] = dicc_vacunas_totales.get(departamento) + dias.get(departamento)
        archivo = "vacunacion.txt"
        print(dicc_vacunas_totales)
        contenido_archivo = open(archivo,"a")
        mostrar_archivo = open(archivo,"r")
        for departamento in dicc_vacunas_totales :
            contenido_archivo.write(departamento)
            contenido_archivo.write(str(dicc_vacunas_totales[departamento])+"\n")
    except IOError :
         return archivo
lista_dep_vacunas = [
{"Montevideo":100,"Maldonado":20,"Canelones":30},
{"Montevideo":150,"Maldonado":40},
{"Montevideo":100,"Canelones":15}
]

print(vacunacion(lista_dep_vacunas))
