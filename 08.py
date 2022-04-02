# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:43:59 2019
@author: Nicolas
"""
#Este programa lee un número entero y determina si la suma de sus dígitos 
#es un número de Fibonacci.

#Esta función retorna la suma de los dígitos del número.
def sum_dig_num(num):
    suma=0
    num=abs(num)
    while num != 0:
    #Cuando sea cero se habrán evaluado todos los dígitos.
        num, a=divmod(num, 10) 
        suma+=a
    return (suma)
#Esta función  retorna el termino "num" de la serie de Fibonacci.
def num_fibonacci(num):
    if num<2:
        return num
        #El término cero es cero y el término uno es uno.
    else:
        a=0
        b=1
        c=0
        for i in range(2, num):
            c=a+b
            a=b
            b=c
        return c
#Captura de errores.
while True:
    try:
        num=int(input("Escriba un número entero: "))
        if type(num)==int:
        #Sí el número es entero.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")
        
#Comparación de la suma de dígitos con cada uno de los términos Fibonacci.
aux=0
num=abs(num)
for i in range (0, (sum_dig_num(num)+3)):
#Se garantiza el mínimo de ciclos necesarios para determinar si la suma de los 
#dígitos es igual a alguno de los términos Fibonacci.
    if sum_dig_num(num)==num_fibonacci(aux):
        print(f"""La suma de los dígitos del número ingresado es \
{sum_dig_num(num)}, {sum_dig_num(num)} es un número fibonacci.""")
        aux=1
        break 
        #Sí los términos resultan ser iguales no es necesario continuar ciclo.
    aux+=1
if aux!=1:
    print(f"""La suma de los dígitos del número ingresado es \
{sum_dig_num(num)}, {sum_dig_num(num)} no es un número Fibonacci.""")

    


    



    