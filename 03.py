# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:55:18 2019
@author: Nicolas
"""
#Este programa lee un número entero positivo y determina la suma de sus
#dígitos pares.

#Esta función determina si un número es par.
def num_es_par(num):
    return (((num//2)*2)==num)
#Esta función determina la suma de los dígitos pares de un número.
def sum_dig_num(num):
    suma=0
    while num != 0:
        num, a=divmod(num, 10) 
        if num_es_par(a):
        #El dígito extraido se almacena en 'a' y en caso de que sea par:
            suma+=a
    return (suma )
#Captura de errores.
while True:
    try:
        num=int(input("Escriba un número entero positivo: "))
        if num>0:
        #Sí el número es un entero positivo.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")
        
print (f"La suma de los dígitos pares de {num} es {sum_dig_num(num)}.")

