def cargar_vector():
    vector = []
    cantidad_numeros = int(input("Ingrese la cantidad de números: "))
    numero = 0
    while cantidad_numeros > 0:
        numero = int(input("Ingrese un número: "))
        vector.append(numero)
        cantidad_numeros -= 1
    return vector

def es_compuesto(numero):
    divisores = 0
    contador = 1
    while contador <= numero:
        if numero % contador == 0:
            divisores += 1
        contador += 1
    return divisores > 2

def mostrar_numeros_compuestos(vector):
    print("Números compuestos:")
    indice = 0
    while indice < len(vector):
        if es_compuesto(vector[indice]):
            print(vector[indice])
        indice += 1

vector = cargar_vector()
mostrar_numeros_compuestos(vector)