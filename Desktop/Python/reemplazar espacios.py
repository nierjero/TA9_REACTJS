cadena="its metal gear, its already active!"
def reemplazar_espacio(cadena):
  cadena_nueva = ""
  for letra in cadena:
     if letra == " ":
         cadena_nueva += ";"
     else:
          cadena_nueva += letra
  return cadena_nueva

print(reemplazar_espacio(cadena))
