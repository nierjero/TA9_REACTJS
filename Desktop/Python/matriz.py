matriz1=[[1,2,3],
         [4,5,6]]

matriz2=[[7,8],
         [9,10],
        [11,12]]

def matriz_multiplicar(matriz1,matriz2) :
  lista_resultados=[]
  sumatorialinea1=0
  fila1= matriz1[0]
  columna1= [fila[0] for fila in matriz2]

  for i in range(len(fila1)) :
     result_linea1= fila1[i]*columna1[i]
     sumatorialinea1=sumatorialinea1+result_linea1
  
  sumatorialinea2=0
  fila1= matriz1[0]
  columna1= [fila[1] for fila in matriz2]

  for i in range(len(fila1)) :
      result_linea1= fila1[i]*columna1[i]
      sumatorialinea2=sumatorialinea2+result_linea1
  lista_resultados.append([sumatorialinea1,sumatorialinea2])
  
  sumatorialinea3=0
  fila1= matriz1[1]
  columna1= [fila[0] for fila in matriz2]

  for i in range(len(fila1)) :
      result_linea1= fila1[i]*columna1[i]
      sumatorialinea3=sumatorialinea3+result_linea1
  
  sumatorialinea4=0
  fila1= matriz1[1]
  columna1= [fila[1] for fila in matriz2]

  for i in range(len(fila1)) :
      result_linea1= fila1[i]*columna1[i]
      sumatorialinea4=sumatorialinea4+result_linea1
  lista_resultados.append([sumatorialinea3,sumatorialinea4])
  
  return lista_resultados

print(matriz_multiplicar(matriz1,matriz2))