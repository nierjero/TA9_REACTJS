def decimal_to_binario(decimal) :
    num_binario_lista = []
    while (decimal/2 !=0) :
      numero_binario = decimal % 2 
      decimal=decimal//2
      num_binario_lista.append(numero_binario)
    lista_invertida = reversed(num_binario_lista)
    print(list(lista_invertida))

decimal = int(input("Ingrese num "))
print(decimal_to_binario(decimal))