import os
os.system ('cls')
#defir variables
nombre= ""
edad = 0
peso = 0.0
altura = 0.0
imc = 0.0
#solicitar informacion
nombre = input ('ingrese su nombre del estudiante: ')
edad = int (input(f'ingrese la edad de {nombre}: '))
peso = float (input(f'ingrese el peso en kg de {nombre}: '))
altura = float (input(f'ingrese la altura en cm de {nombre}: '))
imc = peso /(altura**2)
os.system ('cls')

#hacer las condiciones para dar una respuesta
if (imc>=18.5)and (imc<24.9):
    print(f'el estudiante {nombre} tiene {edad} años de edad' )
    print(f'tiene un imc de {imc:.1f}: esta en un peso normal')
elif (imc>=25)and (imc<29.9):
    print(f'el estudiante {nombre} tiene {edad} años de edad' )
    print(f'tiene un imc de {imc:.1f}: esta en sobrepeso')    
elif (imc>=30)and (imc<34.9):
    print(f'el estudiante {nombre} tiene {edad} años de edad' )
    print(f'tiene un imc de {imc:.1f}: esta en obesidad I')
elif (imc>=35)and (imc<39.9):
    print(f'el estudiante {nombre} tiene {edad} años de edad' )
    print(f'tiene un imc de {imc:.1f}: esta en obesidad II')
else:
    print(f'El estudiante {nombre}\n.tiene {edad} años de edad' )
    print(f'Cuenta con un imc de {imc:.1f}:\n.Esta en sobrepeso')
            
