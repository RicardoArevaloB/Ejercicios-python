import os
os. system('cls')

title="""
------------------------------
-- TORNEO TENIS DE DE MESA --
------------------------------
"""
def determinar_categoria(edad):
    if 15 <= edad <= 17:
        return 'Principiante'
    elif 18 <= edad <= 20:
        return 'Intermedio'
    elif 21 <= edad <= 25:
        return 'Avanzado'
    else:
        return 'Fuera de rango'


jugadores = {'Principiante': [], 'Intermedio': [], 'Avanzado': []}


def registrar_jugador():
    nombre = input('Ingrese el nombre del jugador: ')
    ID = input('Ingrese el ID del jugador: ')
    edad = int(input('Ingrese la edad del jugador: '))
    categoria = determinar_categoria(edad)
    if categoria != 'Fuera de rango':
        if len(jugadores[categoria]) >= 5:
            print(f'Categoría {categoria} llena. No se pueden registrar más jugadores en esta categoría.')
            return
        else:
            jugadores[categoria].append({'ID': ID, 'Nombre': nombre, 'Edad': edad, 'Partidos Ganados': 0, 'Partidos Empatados': 0, 'Partidos Perdidos': 0})
            print(f'Jugador registrado en la categoría {categoria}.')
    else:
        print('Persona fuera del rango de participación.')


def registrar_puntos():
    if not any(jugadores.values()):
        print("No hay jugadores registrados en ninguna categoría.")
        return

    categoria = input('Ingrese la categoría del jugador: ')
    if categoria in jugadores and len(jugadores[categoria]) >= 3:
        ID = input('Ingrese el ID del jugador para registrar puntos: ')
        jugador = next((jugador for jugador in jugadores[categoria] if jugador['ID'] == ID), None)
        if jugador:
            jugador['Partidos Ganados'] = int(input('Ingrese partidos ganados: '))
            jugador['Partidos Empatados'] = int(input('Ingrese partidos empatados: '))
            jugador['Partidos Perdidos'] = int(input('Ingrese partidos perdidos: '))
            print(f"Puntos actualizados para el jugador {jugador['Nombre']}.")
        else:
            print('ID no registrado en esta categoría.')
    else:
        print('No hay suficientes jugadores registrados en esta categoría.')


def mostrar_resultados():
    if not any(jugadores.values()):
        print("No hay jugadores registrados en ninguna categoría.")
        return
    else:
        for categoria, lista_jugadores in jugadores.items():
            if len(lista_jugadores) < 3:
                print(f'No se pueden mostrar resultados para la categoría {categoria} porque no tiene suficientes jugadores registrados.')
                return
        
        for categoria, lista_jugadores in jugadores.items():
            lista_jugadores.sort(key=lambda x: (x['Partidos Ganados'] * 3 + x['Partidos Empatados']), reverse=True)
            print(f"Resultados de la categoría {categoria}:")
            for jugador in lista_jugadores:
                print(f"{jugador['Nombre']} - ID: {jugador['ID']}, Edad: {jugador['Edad']}, Partidos Ganados: {jugador['Partidos Ganados']}, Partidos Empatados: {jugador['Partidos Empatados']}")


def ver_categorias_jugadores():
    if not any(jugadores.values()):
        print("No hay jugadores registrados en ninguna categoría.")
        return
    else:
        print("Categorías y cantidad de jugadores registrados:")
        for categoria, lista_jugadores in jugadores.items():
            print(f"{categoria}: {len(lista_jugadores)} jugadores")


def menu():
    while True:
        print (title)
        print('''
        Menú de selección
        1. Registro de jugadores
        2. Registro de puntos por partido
        3. Resultados
        4. Ver categorías y cantidad de jugadores registrados
        5. Salir
        ''')
        opcion = input('elige una opción: ')
        if opcion == '1':
            registrar_jugador()
        elif opcion == '2':
            registrar_puntos()
        elif opcion == '3':
            mostrar_resultados()
        elif opcion == '4':
            ver_categorias_jugadores()
        elif opcion == '5':
            print('programa finalizado...')
            break
        else:
            print('Opción no válida. Intente de nuevo.')

print(menu())
