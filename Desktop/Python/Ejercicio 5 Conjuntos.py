def conjunto_no_repetido() :
    conjunto = set()
    numero_usuario = int(input("Ingrese un número(-1 para salir) "))
    for i in range(5) :
        if numero_usuario == -1 :
            break
        if numero_usuario in conjunto :
            print("el número ya existía")
        else :
          conjunto.add(numero_usuario)
        if i < 4 :  
            numero_usuario = int(input("Ingrese un número(-1 para salir) "))
    return conjunto

print(conjunto_no_repetido())
    