palabra="snake"

def vocales(palabra) :
    contador=0
    listavocales=["a","e","i","o","u","A","E","I","O","U"]
    for letra in palabra :
        if letra in listavocales :
           contador=contador+1
    return contador

print("La cantidad de vocales en",palabra,"es de",vocales(palabra))

def consonantes(palabra) :
   cant_vocales=vocales(palabra)
   cant_consonantes=palabra[cant_vocales:]
   return len(cant_consonantes)

print("La cantidad de palabras en",palabra,"es de ",consonantes(palabra))
