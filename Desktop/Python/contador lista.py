import random 
n=0
sum = 0

for i in range (20):
    dado1= random.randint (1,6)
    dado2= random.randint (1,6)
    sum = sum + dado1  +dado2
print("El resultado de las 20 tiradas es de ",sum)
