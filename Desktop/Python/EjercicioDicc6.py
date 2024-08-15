def get_artista(cancion) :
    dicc={"Nirvana":"Plain", "Kendrick Lamar":"Compton", "Slowdive":"40 Days", "Dr.Dre":"Compton"}
    print(list(dicc.values()))
    #if cancion in dicc.values() :
      #print(cancion, "es de", dicc[cancion])
      #salir=True
    #else :
     #print("La cancion no esta en la base de datos")
     #cancion=str(input("Ingrese el nombre de la cancion "))

#cancion=str(input("Ingrese el nombre de la cancion "))
get_artista(cancion)