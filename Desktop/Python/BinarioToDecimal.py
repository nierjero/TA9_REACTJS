def binario_to_decimal(binario) :
    suma = 0
    lista_binario = str(binario)
    exp=len(str(binario))
    for digito in str(binario) :
        if digito == 1 :
            suma = suma + 2^exp
            exp=exp-1
    print(suma)
binario = int(input("Ingrese numero binario "))
binario_to_decimal(binario)