import os
ciudades = []
regsismos = []
opcion =0
menu ='1. registrar ciudad \n2. Registrar sismo\n3. buscar sismo por ciudad \n4. informre de riesgo \n5. salir  '

title = """ 
----------------------------
*    REGISTROS DE SISMOS   * 
----------------------------
"""

def registrarciudad():
    addciudad = True
    while (addciudad):
      ciudad = input('Ingrese el nombre de la ciudad: ')
      ciudades.append(ciudad)
      regsismos.append([])  
      addciudad = bool (input('desea registrar otra ciudad: s (si) enter (No)'))

def regsismo():
    addsismo =True
    while(addsismo):
     ciudad = input('Ingrese el nombre de la ciudad que va aregistrar el sismo: ')
     if ciudad in ciudades:
         indice = ciudades.index(ciudad)
         magnitud = float(input('Ingrese la magnitud del sismo: '))
         regsismos[indice].append(magnitud)
         addsismo = bool (input('desea registrar otro sismo: s (si) enter (No)'))
     else:
        print('La ciudad no está registrada.')
        addsismo = bool (input('desea intentarlo de nuevo: s (si) enter (No)'))

def serchsismosciudad():
    ciudad = input('Ingrese el nombre de la ciudad: ')
    if ciudad in ciudades:
        indice = ciudades.index(ciudad)
        print(f'Sismos registrados en {ciudad}:')
        for sismo in regsismos[indice]:
            print(f'Magnitud: {sismo}')
    else:
        print('La ciudad no está registrada.')
        os.system('pause')
        

def inforiesgo():
    for i, ciudad in enumerate(ciudades):
        promedio = sum(regsismos[i]) / len(regsismos[i])
        riesgo = ""
        if promedio < 2.5:
            riesgo = ('Amarillo. (Sin riesgo)')
        elif (promedio <=2.6) and  (promedio <= 4.5):
            riesgo = ('Naranja. (Riesgo medio)')
        else:
            riesgo = ('Rojo. (Riesgo alto)')
        print(f'Ciudad: {ciudad}, Promedio: {promedio:.2f}, Riesgo: {riesgo}')

while (opcion < 5):
    os.system ('cls')
    print (title)
    print (menu)
    
    opcion =int (input(':)_'))

    match (opcion):
        case 1:
         registrarciudad()
        case 2:
         regsismo()
        case 3:
           serchsismosciudad()
           os.system('pause')
        case 4:
          inforiesgo()
          os.system('pause')
        case 5:
          print ('programa finalizado....')
        case _:
          print ('error opcion no valida')
          os.system('pause')
          opcion= 0