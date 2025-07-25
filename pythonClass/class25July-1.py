"""
Autor:
Fecha:
Descripcion:
"""
#Comentario en Linea
"""
Funciones:
    -type: mostrar que tipo de dato es la variable de la cual se desea saber.
    -upper: convertir datos ingresados a Mayuscula.
    -capitalize: convertir con letra capital

Palabras reservadas:
    -pass: omitir condicion
"""

edad = 0
estatura = float(0.0)

#print - mostrar mensaje en consola
print ( type (edad))

#input - Ingresar un valor
edad = int(input('Ingresa tu edad\n'))

#Interpolacion de variables
nombre = input ( 'Ingrese su nombre\n').upper()
print (f'{nombre} Ingrese su edad' , end =': ')
edad = int(input())
estatura = float(input(f'{nombre.capitalize()} Ingrese su estatura :'))

#Estructuras de control Condicionales: if -match(switch)
if (edad > 18):
    print ( f'{nombre} es mayor de edad')
else:
    print ( f'{nombre} es menor de edad')

#Multiples Estructuras de control
if (edad >= 1) and (edad <= 10):
    print ( f'{nombre} es un niño')
elif (edad > 10) and (edad <= 15):
    print ( f'{nombre} es un pre-adolecente')
elif (edad > 15) and (edad < 18):
    print ( f'{nombre} es un adolecente')
else:
    print ( f'{nombre} es mayor de edad')

#Ejercicio 1:
"""
    crear un programa en python que me permita leer el nombre, el salario y la categoria de un
    empleado, las categoria de los empleados estan en:
    a, b y c
    si el empleado es categoria c, se le entrega un bono del 15% adicionado a su salario basico
    si es categoria b, se le entrega un bono del 10% de su salario base
    si es categoria a, el empleado no tiene derecho a bono
    el programa debe imprimir el nombre del empleado, el salario base, la categoria a la que
    pertenece, el valor del bono y el total a pagar
"""

nombre = input('ingrese su nombre \n')
salario = float(input('ingresa tu salario \n'))
categoria = input('ingresa a que categoria perteneces: \n- a\n- b\n- c\n').upper()
bono = float(0.0)
salarioTotal = float(0.0)

if ( categoria == 'C'):
    bono = (salario*0.15)
    salarioTotal = bono + salario

elif ( categoria == 'B'):
    bono = (salario*0.15)
    salarioTotal = bono + salario
else:
    salarioTotal += salario

print( f'{nombre}, tu salario es {salario},\ntu bono es de {bono},\nperteneces a la categoria {categoria},\ntu salario total es de {salarioTotal}')
