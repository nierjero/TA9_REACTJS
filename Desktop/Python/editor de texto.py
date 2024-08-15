def corrector_de_texto() :
  listatextos=[]
  corregirtexto=[]
  cantidadoracion=0
  cantidadcaracteres=0
  textousuario=str(input("ingrese texto: "))
  while textousuario != "::q" :
   t=list(textousuario)
   cantidadoracion=cantidadoracion+1
   cantidadcaracteres=cantidadcaracteres+len(textousuario)
   x = t.pop(0)
   xupper=x.upper()
   t.insert(0,xupper)
   if t[-1] != "." :
    t.append(".")
   textocorregido="".join(t)
   listatextos.append(textocorregido)
   textousuario=str(input("ingreso texto: "))
  return listatextos,cantidadcaracteres, cantidadoracion
  

print(corrector_de_texto())