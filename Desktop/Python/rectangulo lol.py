lista=[]
listapares=[]
n=int(input())
while n >= 0 :
    lista.append(n)
    if n % 2 == 0 :
        listapares.append(n)
    n=int(input())
print(lista)
print(listapares)
