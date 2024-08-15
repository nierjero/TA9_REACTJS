def min_avg_max() :
    listanúmeros=[]
    lista_minimo_maximo_promedio=[]
    contador=0
    sumatoria=0
    promedio=0
    número=int(input("Ingrese un número(Ingrese 0 para terminar) "))
    listanúmeros.append(número)
    max=número
    min=número
    while número != 0 :
        listanúmeros.append(número)
        sumatoria+=número
        if número>max :
            max=número
        elif número<min :
            min=número
        contador+=1
        número=int(input("Ingrese un número(Ingrese 0 para terminar) "))
    promedio=sumatoria/contador
    lista_minimo_maximo_promedio.append(min)
    lista_minimo_maximo_promedio.append(max)
    lista_minimo_maximo_promedio.append(promedio)
    return lista_minimo_maximo_promedio


print(min_avg_max())