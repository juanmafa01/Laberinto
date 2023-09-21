import csv
laberinto = []
with open('ejemplo.csv', mode= 'r', newline='' ) as csvArchivo:

    lector_csv = csv.reader(csvArchivo, delimiter=';')

    for fila in lector_csv:
        laberinto.append([int(celda) for celda in fila])


for fila in laberinto:
     print(','.join(map(str, fila)))



def encontrar_todos_los_caminos(laberinto, fila, columna, salida_fila, salida_columna, camino_actual=[], todos_los_caminos=[]):
    if fila < 0 or fila >= len(laberinto) or columna < 0 or columna >= len(laberinto[0]) or laberinto[fila][columna] != 0:
        return

    if fila == salida_fila and columna == salida_columna:
        camino_actual.append((fila, columna))
        todos_los_caminos.append(list(camino_actual))
        camino_actual.pop()
        return

    camino_actual.append((fila, columna))
    laberinto[fila][columna] = -1

    encontrar_todos_los_caminos(laberinto, fila - 1, columna, salida_fila, salida_columna, camino_actual, todos_los_caminos)
    encontrar_todos_los_caminos(laberinto, fila + 1, columna, salida_fila, salida_columna, camino_actual, todos_los_caminos)
    encontrar_todos_los_caminos(laberinto, fila, columna - 1, salida_fila, salida_columna, camino_actual, todos_los_caminos)
    encontrar_todos_los_caminos(laberinto, fila, columna + 1, salida_fila, salida_columna, camino_actual, todos_los_caminos)

    camino_actual.pop()
    laberinto[fila][columna] = 0

def encontrar_todos_caminos(laberinto, entrada, salida):
    fila_entrada, columna_entrada = entrada
    fila_salida, columna_salida = salida

    todos_los_caminos = []
    encontrar_todos_los_caminos(laberinto, fila_entrada, columna_entrada, fila_salida, columna_salida, [], todos_los_caminos)
    return todos_los_caminos



def encontrar_entrada_y_salida(laberinto):
    entrada = None
    salida = None

    # Buscar la entrada y la salida en las filas superiores e inferiores del laberinto
    for fila in [0, len(laberinto) - 1]:
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == 0:
                if entrada is None:
                    entrada = (fila, columna)
                else:
                    salida = (fila, columna)
                if entrada is not None and salida is not None:
                    return entrada, salida

    # Buscar la entrada y la salida en las columnas izquierda y derecha del laberinto
    for columna in [0, len(laberinto[0]) - 1]:
        for fila in range(len(laberinto)):
            if laberinto[fila][columna] == 0:
                if entrada is None:
                    entrada = (fila, columna)
                else:
                    salida = (fila, columna)
                if entrada is not None and salida is not None:
                    return entrada, salida

    if entrada is None or salida is None:
        raise ValueError("No se encontró una entrada o salida válida en el laberinto.")

    return entrada, salida

entrada, salida = encontrar_entrada_y_salida(laberinto)
print(f"La entrada está en la posición: {entrada}")
print(f"La salida está en la posición: {salida}")

entrada, salida = encontrar_entrada_y_salida(laberinto)

todos_los_caminos = encontrar_todos_caminos(laberinto, entrada, salida)

for i, camino in enumerate(todos_los_caminos, start=1):
    print(f"Camino {i}:")
    for fila, columna in camino:
        print(f"({fila}, {columna})")
    print()
    


import tkinter as tk

# Crea una ventana de Tkinter
ventana = tk.Tk()
ventana.title("Laberinto")

# Configura las dimensiones del laberinto
filas = len(laberinto)
columnas = len(laberinto[0])
ancho_celda = 40

# Crea un lienzo (canvas) para dibujar el laberinto
lienzo = tk.Canvas(ventana, width=ancho_celda * columnas, height=ancho_celda * filas)
lienzo.pack()

# Define los colores para las celdas del laberinto
colores = {
    0: "white",  # Pasillo
    1: "black",  # Pared
    -1: "green",  # Entrada
    -2: "red",  # Salida
}

# Dibuja el laberinto en el lienzo
for fila in range(filas):
    for columna in range(columnas):
        valor = laberinto[fila][columna]
        color = colores[valor]
        x1 = columna * ancho_celda
        y1 = fila * ancho_celda
        x2 = x1 + ancho_celda
        y2 = y1 + ancho_celda
        lienzo.create_rectangle(x1, y1, x2, y2, fill=color)

# Ejecuta la aplicación
ventana.mainloop()
