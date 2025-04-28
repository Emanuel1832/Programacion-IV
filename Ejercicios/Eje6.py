def cargar_equipos():
    equipo = []
    while True:
        campeon = input("Ingrese el nombre de un campeón o 'fin' para terminar: ")
        if campeon.lower() == 'fin':
            break
        equipo.append(campeon)
    return equipo

def agregar_asistente(equipo, asistente):
    equipo_con_asistentes = []
    for campeon in equipo:
        equipo_con_asistentes.append(campeon)
        if campeon == asistente:
            equipo_con_asistentes.append("Nami")
    return equipo_con_asistentes

mi_equipo = cargar_equipos()
asistente = input("Ingrese el nombre del asistente: ")
nuevo_equipo = agregar_asistente(mi_equipo, asistente)
print("Equipo resultante:", nuevo_equipo)