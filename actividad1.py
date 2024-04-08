import random

def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(random.randint(1, 40)) 
        matriz.append(fila)
    return matriz

filas = int(input("Por favor, ingresa el número de filas para la matriz: "))
columnas = int(input("Por favor, ingresa el número de columnas para la matriz: "))

matriz = crear_matriz(filas, columnas)

print("Matriz creada:")

for fila in matriz:
    print(fila)
def feedback(filas, columnas):
    if filas <= 1 or columnas <= 1:
        feed = input("Al menos una de las dimensiones ingresadas no es mayor o igual a uno. Por favor ingresa valores válidos: ")
        return feed

    return None

feedback_msg = feedback(filas, columnas)
while feedback_msg:
    filas = int(input(feedback_msg + " "))
    columnas = int(input("Ahora por favor dime un numero mayor o igual a uno para colocar columnas en la matriz: "))
    feedback_msg = feedback(filas, columnas)

filaEsp = random.randint(filas, columnas)
colEsp = random.randint(filas, columnas)
especial = "*"

matriz.append(filaEsp) #no sería .append, eso pushea un elemento al final de la matriz en este caso
matriz.append(colEsp)
matriz.append(especial)

print(matriz)
