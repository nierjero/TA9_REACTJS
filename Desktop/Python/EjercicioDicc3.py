#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número
#de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
#informando de ello. Repetir las preguntas hasta que el usuario
#ingrese la palabra  fin (fin puede estar en mayúsculas o minúsculas).

dicc = {"Banana":1.35 , "Manzana":0.80 , "Pera":0.85 , "Naranja":0.70}
salir=False
while not salir :
      fruta=str(input("Ingrese una fruta (fin para salir) "))
      if fruta != "fin" and fruta != "FIN" and fruta != "Fin" :
           if fruta in dicc :
              kilos=int(input("Ingrese cuantos kilos "))
              print("El precio a pagar es de ", (dicc[fruta]*kilos))
           else :
                print("La fruta no esta disponible")
      else :
         print("Pague en caja")
         salir=True
