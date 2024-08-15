def convertir_decimal() :
    dicc_hexadecimal = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    sumatoria = 0
    numero = str(input("Ingrese un numero "))
    base = int(input("Ingrese la base "))
    index = len(numero)-1
    if base == 2 or base == 16 :
        for digito in numero :
            if digito not in dicc_hexadecimal :
                digito_int = int(digito)
                confirmar_numero_negativo = int(numero)*-1
                if numero == abs(int(numero)) :
                    print("No se pueden ingresar números negativos")
                    break
                sumatoria += digito_int * (base**index)
                index += - 1
            else :
                digito = int(dicc_hexadecimal[digito])
                sumatoria += digito * (base**index)
                index += - 1
    else :
        print("La base debe ser 2 o 16")
            
                
    return sumatoria

print(f"Resultado:{convertir_decimal()}")