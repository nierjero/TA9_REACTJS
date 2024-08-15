valor_billetes=[100,50,10,5,2,1]
precio=150
def billetes(valor_billetes,precio) :
    contador=0
    for valores in valor_billetes :
        contador=0
        while precio >= valores :
            contador=contador+1
            precio=precio-valores
            if contador>0 :
              print(valores,"x",contador)    

billetes(valor_billetes,precio)  

