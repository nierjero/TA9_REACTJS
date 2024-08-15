listaesp = ["hoy","es","viernes"]
listaing = ["today","is","friday"]
frase = "Hoy es viernes"

def traducir(listaesp,listaing,frase):
    print (frase)
    frase = frase.split(" ")

    fraseTrad=[]
    for element in frase:
        if element in listaesp:
            for i in range(len(listaesp)):
                if listaesp[1]==element:
                    fraseTrad.append(listaing[i])
    
    resultado = " ".join(fraseTrad)
    return resultado


print(traducir(listaesp,listaing,frase))