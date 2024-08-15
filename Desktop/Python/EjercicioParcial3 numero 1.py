def perrosYPelota(xyz):
 try :
   distancia_perro_A_pelota = xyz[2] - xyz[0]
   distancia_perro_B_pelota = xyz[2] - xyz[1]

   if abs(distancia_perro_B_pelota) > abs(distancia_perro_A_pelota) :
     print("Gano el perro A")
   elif abs(distancia_perro_A_pelota) > abs(distancia_perro_B_pelota) :
      print("Gano el perro B")
   else :
      print("La pelota rebotó, ambos llegaron a la misma vez")
 except TypeError :
   print("Se ingresó un string en vez de un número")   
 except IndexError :
   print("Faltan elementos en la lista")


xyz = [1,21,10]
perrosYPelota(xyz)