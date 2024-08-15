# Crear un diccionario vacío
diccionario = {}

# Crear un diccionario con elementos iniciales
diccionario = {'clave1': valor1, 'clave2': valor2, 'clave3': valor3}

# Acceder a un valor utilizando una clave
valor = diccionario['clave']

# Agregar un nuevo par clave-valor al diccionario
diccionario['nueva_clave'] = nuevo_valor

# Verificar si una clave existe en el diccionario
if 'clave' in diccionario:
    # La clave existe

# Eliminar una clave y su valor del diccionario
del diccionario['clave']

# Obtener todas las claves del diccionario
claves = diccionario.keys()

# Obtener todos los valores del diccionario
valores = diccionario.values()

# Obtener pares clave-valor como tuplas
items = diccionario.items()

# Recorrer las claves y valores del diccionario
for clave, valor in diccionario.items():
    # Hacer algo con la clave y el valor

# Obtener el número de elementos en el diccionario
num_elementos = len(diccionario)

# Copiar un diccionario
copia_diccionario = diccionario.copy()

# Limpiar todos los elementos del diccionario
diccionario.clear()

# Comprobar si un diccionario está vacío
if not diccionario:
    # El diccionario está vacío

# Combinar dos diccionarios en uno solo
diccionario1.update(diccionario2)

# Obtener un valor por defecto si la clave no existe en el diccionario
valor = diccionario.get('clave', valor_por_defecto)

#Crear un nuevo diccionario con las claves especificadas y un valor por defecto para todas las claves.
dict.fromkeys(una_lista_por_ejemplo)
