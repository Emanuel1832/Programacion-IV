def cargar_datos():
    matriz = []
    fila_actual = 1
    while True:
        numeros_ingresados = input(f"Ingrese los números de la fila {fila_actual} separados por espacio y 'fin' para acabar: ")
        if numeros_ingresados.lower() == "fin":
            break
        fila = [int(valor) for valor in numeros_ingresados.split()]
        matriz.append(fila)
        fila_actual += 1
    return matriz

def calcular_promedio_de_cada_fila(datos):
    promedios_filas = []
    for fila in datos:
        suma_fila = sum(fila)
        cantidad_numeros_fila = len(fila)
        promedio_fila = suma_fila / cantidad_numeros_fila
        promedios_filas.append(promedio_fila)
    return promedios_filas

def calcular_promedio_vertical(datos):
    if not datos:
        return []
    promedios_columnas = []
    for columna_index in range(len(datos[0])):
        columna = [fila[columna_index] for fila in datos]
        suma_columna = sum(columna)
        cantidad_numeros_columna = len(columna)
        promedio_columna = suma_columna / cantidad_numeros_columna
        promedios_columnas.append(promedio_columna)
    return promedios_columnas

def mostrar_matriz(datos):
    for fila in datos:
        print(fila)

datos_ingresados = cargar_datos()
promedios_filas = calcular_promedio_de_cada_fila(datos_ingresados)
promedios_columnas = calcular_promedio_vertical(datos_ingresados)

print("\nMatriz ingresada:")
mostrar_matriz(datos_ingresados)
print("\nPromedios de cada fila:", promedios_filas)
print("Promedios de cada columna:", promedios_columnas)