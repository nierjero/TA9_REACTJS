from ultimodigitoprimerdigito import ultimodigito
from ultimodigitoprimerdigito import sacarultimodigito
print("Ingrese un número")
num=int(input())
sumatoria=0
while num > 0 :
    ultimo_digito=ultimodigito(num)
    sumatoria+=ultimo_digito
    num=sacarultimodigito(num)
    
print(sumatoria)