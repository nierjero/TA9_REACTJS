listadelistas=[[1,2],[1,3,4],[4],[1,7,-3,9]]

def promedio_listas(listadelistas):
    promediolistas=[]
    sumatorialista1=0
    for lista in listadelistas :
       sumatorialista1=0
       for elemento in lista :
        promedio=len(lista)
        sumatorialista1=sumatorialista1+elemento
        promedio1=(sumatorialista1)/(promedio)
       promediolistas.append(promedio1) 
    return promediolistas

print(promedio_listas(listadelistas))

