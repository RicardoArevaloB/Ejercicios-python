import os
os.system('cls')

pesoideal=0
obesidadI= 0
obesidadII = 0
obesidadIII = 0
sobrepeso = 0

for i in range (0,2,1):
    peso= float (input(f'ingrese el peso en (kg) del estudiante {i+1}: '))
    altura = float(input(f'ingrese la altura en (m) del estudinate {i+1}: '))
    imc = (peso/(altura **2))
    if (imc>=18.5)and (imc<24.9):
      pesoideal += 1
    elif (imc>=25)and (imc<29.9):
      sobrepeso += 1 
    elif (imc>=30)and (imc<34.9):
      obesidadI +=1 
    elif (imc>=35)and (imc<39.9):
      obesidadII += 1
    else:
     obesidadIII +=1
    
os.system('cls')
print (f'a. estudiantes se encuentran en el peso ideal. {pesoideal}')
print (f'b. estudiantes se encuentran en obesidad grado I {obesidadI}')
print(f'c. estudiantes se encuentran en obesidad grado II {obesidadII}')
print(f'd. estudiantes se encuentran en obesidad grado III {obesidadIII}')
print(f'e. estudiantes se encuentran en Sobrepeso {sobrepeso}')


