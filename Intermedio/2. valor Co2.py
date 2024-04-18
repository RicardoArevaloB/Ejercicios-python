import os
os.system('cls')
opcion=0
menu= '1. Registrar Dependencia\n2. Registrar Consumo por Dependencia\n3. Ver CO2 Producido\n4. Dependencia que Produce Mayor CO2\n5. Salir'
title="""
------------------
* CALCULAR CO2  *
------------------
"""

class Dependencia:
    def __init__(can,nombre,):
        can.nombre = nombre
        can.consumoelectricidad = 0  
        can.consumodispositivos = 0  
        can.aparatoselectricos = 0 
    def addconsumoelectrico (can, consumo):
        can.consumoelectricidad += consumo

    def addconsumodispositivos(can, consumo):
        can.consumodispositivos += consumo

    def addemisionestransportes(can, emisiones):
        can.aparatoselectricos += emisiones

    def calcularemisionestotales(can, factoremisionelectricidad):
        emisioneselectricidad = can.consumoelectricidad * factoremisionelectricidad
        emisionestotales = emisioneselectricidad + can.consumodispositivos + can.aparatoselectricos
        return emisionestotales

dependencias = []

def regdependencia():
    adddependecia = True
    while (adddependecia):
        nombre = input("Ingrese el nombre de la dependencia: ")
        dependencia = Dependencia(nombre)
        dependencias.append(dependencia)
        print("Dependencia registrada correctamente.")
        adddependecia= bool(input('desea registrar otra dependencia (S) si. (Enter) no. '))

def regconsumodependencia():
    regconsumodepen=True
    while (regconsumodepen):
        nombredependencia = input("Ingrese el nombre de la dependencia: ")
        for dependencia in dependencias:
            if dependencia.nombre == nombredependencia:
                consumoelectricidad = float(input("Ingrese el consumo de electricidad en kWh: "))
                consumodispositivos = float(input("Ingrese el consumo de dispositivos en kWh: "))
                
                dependencia.addconsumoelectrico(consumoelectricidad)
                dependencia.addconsumodispositivos(consumodispositivos)
                print("Consumo registrado correctamente para la dependencia", nombredependencia)
                return
        print('La dependencia no se encuentra registrada.')
        
def CO2producido():
    for dependencia in dependencias:
        print('Dependencia:', dependencia.nombre)
        print('CO2 producido:', dependencia.calcularemisionestotales(factor_emision_electricidad))
        print()

def depenmayorCO2():
    mayoremisiones = 0
    dependenciamayor = None
    for dependencia in dependencias:
        emisiones = dependencia.calcularemisionestotales(factor_emision_electricidad)
        if emisiones > mayoremisiones:
            mayoremisiones = emisiones
            dependencia_mayor = dependencia.nombre
    if dependenciamayor:
        print('La dependencia que produce mayor CO2 es:', dependenciamayor)
    else:
        print('No se han registrado dependencias.')

factor_emision_electricidad = 0.5  


while (opcion < 5):
    os.system('cls')
    print (title)
    print (menu)

    opcion = int(input('Eliga una de las opciones: '))

    match (opcion):
        case 1:
            regdependencia()
            os.system('pause')         
        case 2:
            regconsumodependencia()
            os.system('pause') 
        case 3: 
            CO2producido()
            os.system('pause') 
        case 4: 
            depenmayorCO2()
            os.system('pause') 
        case 5: 
            print('Hasta luego....')
            os.system('pause') 
        case _:
            print('Opción no válida. Por favor, seleccione una opción válida.')
            os.system('cls')    