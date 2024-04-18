import os 
os.system('cls')

totalnum = 0
tnumerospares = 0
snumerospares = 0
snumerosimpares = 0
numenoresq10 = 0
numentre20y50 = 0
numayoresq100 = 0

while True:
    numero = int (input('ingrese un numero entero poditivo y para finalizar ingrese un numero negativo '))
    if (numero > 0):
        totalnum += 1
    else:    
        break
    if (numero % 2 == 0):
       tnumerospares += 1
       snumerospares += numero
    else:
        snumerosimpares += numero  
    if (numero < 10):
       numenoresq10 += 1
    elif (numero >= 20)and(numero <= 50):
        numentre20y50 += 1
    elif (numero > 100):
        numayoresq100 += 1
if (tnumerospares >0):
    prompares = snumerospares / totalnum
else:
    prompares = 0


if (totalnum - tnumerospares) >0:
    promimpares = snumerosimpares / totalnum
else:
    promimpares = 0     

os.system('cls')
print ('informe de los numeros igresados')

print (f'Total de números ingresados {totalnum}')   
print(f'Total de números pares ingresados {tnumerospares}')
print (f'Promedio de los números pares {prompares}')
print (f'Promedio de los números impares {promimpares}')
print (f'Cuantos números son menores que 10 {numenoresq10}')
print (f'Cuantos números están entre 20 y 50 {numentre20y50}')
print (f'Cuantos números son mayores que 100 {numayoresq100}')
    



