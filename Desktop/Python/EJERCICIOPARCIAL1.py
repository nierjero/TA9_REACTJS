
texto="Hola están? mundo, como están?"
palabra="están?"
def buscar_palabra(texto,palabra) :
    posición=[]
    textolista=texto.split()
    for elemento in range(len(textolista)) :
        if textolista[elemento]==palabra :
         posición.append(elemento)
    return posición   
 
print(buscar_palabra(texto,palabra))