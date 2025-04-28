def Cargar_lista():
    lista = []
    while True:
        num = input("Ingrese un num y 'fin' para terminaer : ")
        if num.lower() == 'fin':
            break
        lista.append(float(num))
    return lista

def Veri_ent(digitos):
    parte_entera = str(int(abs(digitos))) 
    digitos_pares = 0
    digitos_impares = 0

    for digito in parte_entera:
        if int(digito) % 2 == 0: 
            digitos_pares += 1
        else: 
            digitos_impares += 1
    return digitos_pares == 2 or digitos_impares >= 2

def filtrar_lista(lista1):
    lista_b = []
    for numero in lista1:
        if Veri_ent(numero):
            lista_b.append(numero)
    return lista_b

def mostrar_resultado(lista_b):
    print("Lista B (con los números que cumplen las condiciones):")
    for num in lista_b:
        print(num)

lista_a = Cargar_lista() 
lista_b = filtrar_lista(lista_a) 
mostrar_resultado(lista_b)