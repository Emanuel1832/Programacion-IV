def ingresar_numero():
    
    numeros = int(input("Ingrese un numero : "))
    return numeros

def contar_digitos(num0):

    impares = len(str(abs(num0)))  
    return impares

def mostrar_resultado(cantidad):

    print("Cantidad de dígitos:", cantidad)

numero1 = ingresar_numero()
can_num = contar_digitos(numero1)
mostrar_resultado(can_num)