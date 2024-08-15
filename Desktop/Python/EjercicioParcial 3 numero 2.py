import random
def lista_magica(num1,num2,num3) :
   magic = set()
   if num1 < 0 :
     return []
   elif num2 == num3 :
     return []
   elif num3-num2 < 0 :
     return []
   elif num3-num2<num1 :
     return []
   magic = set()
   while len(magic) < num1 :
        magic.add(random.randint(num2, num3))
   return list(magic)

num1 = 10
num2 = 6
num3 = 2
print(lista_magica(num1,num2,num3))