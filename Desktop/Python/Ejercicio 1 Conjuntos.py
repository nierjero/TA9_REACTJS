a={"juan","pepe","maria","jose","esteban","lucia"}

b={"juan","pepe","marta","lucia","john"}

c={"lucia","john","maria","esteban","margarita"}

todos=a|b|c 
todos.add("snake")

ByC= b & c
CyA= c & a
AyB= a & b 
CyByA= c & b & a 
DosRevistas= ByC | CyA  | AyB
UnaRevista= a-b-c  | c-b-a  | b-c-a
NingunaRevista= todos-a-b-c
print("Personas que leen Revista B y C:" ,ByC)
print("Personas que leen Revista C y A:", CyA)
print("Personas que leen Revista C y B:", AyB)
print("Personas que leen las tres Revistas:", CyByA)
print("Personas que leen dos revistas",DosRevistas)
print("Personas que leen una revista",UnaRevista)
print("Quienes no leen ninguna revista son",NingunaRevista)