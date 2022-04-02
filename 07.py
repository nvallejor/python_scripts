# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:27:15 2019

@author: Nicolas
"""
#Este programa lee un número entero positivo, determina si existen en el número
#dígitos repetidos y reporta cuales son los dígitos repetidos.

#Esta función determina cuantas veces (times) se repite un dígito (dig).
def det_cuantos_dig(num, dig): 
    times=0
    while num != 0:
    #Cuando num sea igual a cero quiere decir 
    #que se ha obtenido el último dígito.
        num, a=divmod(num, 10) 
        if a==dig:
        #Sí 'a' el dígito extraido es igual a 'dig', el dígito ingresado. 
            times+=1
    return (times, dig)
#Captura de errores.
while True:
    try:
        num=int(input("Escriba un número entero positivo: "))
        if 0<num:
        #Sí el número es entero positivo.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")
        
#Determinar si tiene o no dígitos repetidos.
aux=0
for i in range (0,10):
#Se evaluan uno por uno los diez dígitos posibles.
    times, dig = det_cuantos_dig(num, i)
    if times>1:
    #Sí el dígito i se repite.
        print("El número tiene dígitos repetidos:")
        aux=1
        break
if aux!=1:
#Si el número no se repite.
    print ("El número no tiene dígitos repetidos.")
    
#Determinar cuales son los dígitos repetidos.
for i in range (0,10):
#Se evaluan uno por uno los diez dígitos posibles.
    times, dig=det_cuantos_dig(num, i)
    if times>1:
        print (f"\u2981 El dígito {dig} se repite {times} veces.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
