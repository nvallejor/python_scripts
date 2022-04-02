# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:09:04 2019

@author: Nicolas
"""
#Este programa lee un número entero positivo de máximo 5 dígitos y determina
#cual de sus dígitos es el mayor.

#Esta función determina cuál de los dígitos de un número es el mayor.
def det_mayor(num):
    mayor=1
    while num != 0:
        num, a=divmod(num, 10) 
        #En 'a' se almacena el dígito extraido.
        if mayor<a:
            mayor = a
            #Se va guardando el mayor dígito.
    return (mayor)
#Captura de errores.
while True:
    try:
        num=int(input("Escriba un número entero positivo de máximo 5 \
dígitos: "))
        if 0<num<100000:
        #Sí el número es un entero positivo.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")      
        
print (f"El mayor dígito de {num} es {det_mayor(num)}.")
