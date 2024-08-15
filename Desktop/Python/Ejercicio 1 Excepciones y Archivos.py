salir=False
while not salir :
  try:
     celsius=float(input("Ingrese el valor númerico de los grados Celsius "))
     fahrenheit= (celsius*(9/5))+32
     print("Los grados en Fahrenheit son ", fahrenheit ,"°F")
     salir=True
  except :
     print("sos mogolico, ingresá bien")
 
 
   