import random 

def generar_contraseña() :
    contraseña=[] 
    n=int(input("Ingrese cuantos dígitos quiere que tenga su contraseña :"))
    for i in range(n) :
        num=random.randint(1,9)
        contraseña.append(num)
    for i in contraseña :
        ",".join(str(contraseña))
    return contraseña 

print("Su contraseña generada es ",generar_contraseña())