# Abrir el archivo y leer todas las líneas
with open('archivo.txt', 'r') as archivo:
    lineas = archivo.readlines()

# Crear una lista vacía para almacenar las líneas deseadas
lineas_deseadas = []

# Recorrer todas las líneas del archivo
for i, linea in enumerate(lineas):
    # Omitir las líneas a eliminar
    if i+1 in [1, 2, 3, 34, 35, 66]:
        continue
    # Agregar las líneas deseadas a la lista
    lineas_deseadas.append(linea.strip())

tuplas = []
for i in range(0, len(lineas_deseadas), 3):
    elementos = lineas_deseadas[i:i+3]
    tupla = tuple(elementos)
    tuplas.append(tupla)

# Eliminar el elemento 3 de todas las tuplas en tuplas
for i, tupla in enumerate(tuplas):
    tuplas[i] = tupla[:2] + tupla[3:]

# Crear las dos listas de tuplas utilizando cortes
lista1 = tuplas[0:10]
lista2 = tuplas[10:]

# Eliminar todas las comas de los elementos de lista1
for i, tupla in enumerate(lista1):
    lista1[i] = tuple(elemento.replace(',', '') for elemento in tupla)

# Eliminar todas las comas de los elementos de lista2
for i, tupla in enumerate(lista2):
    lista2[i] = tuple(elemento.replace(',', '') for elemento in tupla)

# Convertir los elementos de lista1 a flotantes
for i, tupla in enumerate(lista1):
    for j, elemento in enumerate(tupla):
        lista1[i] = tuple(float(elemento.replace(',', '')) for elemento in tupla)

# Convertir los elementos de lista2 a flotantes
for i, tupla in enumerate(lista2):
    for j, elemento in enumerate(tupla):
        lista2[i] = tuple(float(elemento.replace(',', '')) for elemento in tupla)



# Buscar el valor más grande en el índice 1 de las tuplas de lista1
max_valor = -float('inf')
max_indice = None
for i, tupla in enumerate(lista1):
    if tupla[1] > max_valor:
        max_valor = tupla[1]
        max_indice = i

lista1_maximo_1 = lista1[max_indice][0]
# Imprimir el índice 0 de la tupla que tiene el valor más grande en el índice 1
#print("lista1_maximo_1 de lista1 es:", lista1_maximo_1)

max_valor = -float('inf')
max_indice = None
for i, tupla in enumerate(lista2):
    if tupla[1] > max_valor:
        max_valor = tupla[1]
        max_indice = i

# Imprimir el índice 0 de la tupla que tiene el valor más grande en el índice 1
#print("El índice 0 de la tupla con el valor más grande en el índice 1 de lista2 es:", lista2[max_indice][0])

# Obtener el valor del índice 0 de la tupla con el valor máximo en el índice 1 de lista2
max_valor = -float('inf')
max_indice = None
for i, tupla in enumerate(lista1):
    if tupla[1] > max_valor:
        max_valor = tupla[1]
        max_indice = i

max_valor_0 = lista1[max_indice][0]

# Eliminar las tuplas de lista1 cuyo valor en el índice 0 sea mayor que max_valor_0
lista1 = [tupla for tupla in lista1 if tupla[0] > max_valor_0]

#print("La lista1 actualizada es:", lista1)

# Elimina las tuplas no necesarias de lista2
# Obtener el valor del índice 0 de la tupla con el valor máximo en el índice 1 de lista2
max_valor = -float('inf')
max_indice = None
for i, tupla in enumerate(lista2):
    if tupla[1] > max_valor:
        max_valor = tupla[1]
        max_indice = i
max_valor_0 = lista2[max_indice][0]
lista2_maximo_1 = max_valor_0

#print("lista2_maximo_1 de lista2 es:",lista2_maximo_1)
# Eliminar las tuplas de lista2 cuyo valor en el índice 0 sea mayor que max_valor_0
lista2 = [tupla for tupla in lista2 if tupla[0] < max_valor_0]

# Imprimir la lista2 actualizada
#print("La lista2 actualizada es:", lista2)

# Añadir un tercer valor a cada tupla de lista1 que represente la multiplicación de los valores en el índice 0 y 1
for i, tupla in enumerate(lista1):
    lista1[i] = tupla + (tupla[0] * tupla[1],)

# Imprimir la lista1 actualizada
#print("La lista1 actualizada es:", lista1)

# Añadir un tercer valor a cada tupla de lista2 que represente la multiplicación de los valores en el índice 0 y 1
for i, tupla in enumerate(lista2):
    lista2[i] = tupla + (tupla[0] * tupla[1],)

# Imprimir la lista2 actualizada
#print("La lista2 actualizada es:", lista2)

# Calcular la variable promedio
suma_valor3 = sum([tupla[2] for tupla in lista1])
suma_valor2 = sum([tupla[1] for tupla in lista1])
promedio = suma_valor3 / suma_valor2

# Imprimir el resultado
#print("El valor promedio de lista1 es:", promedio)

# Calcular la variable promedio para lista2
suma_valor3_2 = sum([tupla[2] for tupla in lista2])
suma_valor2_2 = sum([tupla[1] for tupla in lista2])
promedio_2 = suma_valor3_2 / suma_valor2_2

# Imprimir el resultado
#print("El valor promedio_2 de lista2 es:", promedio_2)

# Eliminar las tuplas de lista1 que tengan un valor1 mayor a promedio
nueva_lista1 = []
for tupla in lista1:
    valor1, valor2, valor3 = tupla
    if valor1 > promedio:
        nueva_lista1.append(tupla)

# Asignar la nueva lista1 a la variable original
lista1 = nueva_lista1

#print(lista1)

# Eliminar las tuplas de lista2 que tengan un valor1 menor a promedio_2
nueva_lista2 = []
for tupla in lista2:
    valor1, valor2, valor3 = tupla
    if valor1 < promedio_2:
        nueva_lista2.append(tupla)

# Asignar la nueva lista2 a la variable original
lista2 = nueva_lista2


#print(lista2)

# Obtener el maximo valor por encima del promedio de la lista1
max_valor2 = -float('inf')
max_valor1 = None

for tupla in lista1:
    if tupla[1] > max_valor2:
        max_valor2 = tupla[1]
        max_valor1 = tupla[0]

lista1_maximo_2 = max_valor1

#print("lista1_maximo_2 de lista1 es:",lista1_maximo_2)

# Obtener el maximo valor por encima del promedio de la lista2
max_valor2 = -float('inf')
max_valor1 = None

for tupla in lista2:
    if tupla[1] > max_valor2:
        max_valor2 = tupla[1]
        max_valor1 = tupla[0]

lista2_maximo_2 = max_valor1


# calculando las distancias
distancia_max1_max2_short = ((lista1_maximo_1 - lista1_maximo_2)/lista1_maximo_1)*-100
distancia_max1_prom_short = ((lista1_maximo_1 - promedio)/lista1_maximo_1)*-100
distancia_max1_max2_long = ((lista2_maximo_2 - lista2_maximo_1)/lista2_maximo_1)*-100
distancia_max1_prom2_long = ((promedio_2 - lista2_maximo_1)/lista2_maximo_1)*-100

precio_entrada_short = lista1_maximo_1
precio_stop_short = promedio if distancia_max1_max2_short > 5 else lista1_maximo_2
precio_entrada_long = lista2_maximo_1
precio_stop_long = promedio_2 if distancia_max1_max2_long > 5 else lista2_maximo_2

'''
print("lista1_maximo_1 de lista1 es:", lista1_maximo_1)
print("lista2_maximo_1 de lista2 es:",lista2_maximo_1)
print("El valor promedio de lista1 es:", promedio)
print("El valor promedio_2 de lista2 es:", promedio_2)
print("lista1_maximo_2 de lista1 es:",lista1_maximo_2)
print("lista2_maximo_2 de lista2 es:",lista2_maximo_2)
print(distancia_max1_max2_short)
print(distancia_max1_prom_short)
'''