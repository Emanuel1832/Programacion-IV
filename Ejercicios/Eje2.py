def separar_numero_en_partes(numero):
    numero_como_texto = str(numero)
    if '.' in numero_como_texto:
        parte_entera, parte_decimal = numero_como_texto.split('.')
    else:
        parte_entera, parte_decimal = numero_como_texto, ''
    return parte_entera, parte_decimal

def contar_caracteres(cadena):
    return len(cadena)

def mostrar_info_numero(numero):
    entero, decimal = separar_numero_en_partes(numero)
    print(f"Dígitos en la parte entera: {contar_caracteres(entero)}")
    print(f"Dígitos en la parte decimal: {contar_caracteres(decimal)}")

numero_ingresado = float(input("Ingrese un número decimal: "))
mostrar_info_numero(numero_ingresado)