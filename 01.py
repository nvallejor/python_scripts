# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:27:15 2019
@author: Nicolas
"""
#Este programa lee un número entero de 3 dígitos y determina si contiene el
#dígito 1.

#Esta función determina si el número 'num' contiene el dígito 1.
def det_si_dig1(num):
    aux=0
    while num != 0:
        num, a=divmod(num, 10) 
        #Se almacena provisionaalmente el dígito en 'a'.
        if a==1:
            aux=1
    return (aux==1)
    #Verdadero cuando el número 'num' contenga eldígito 1.
#Captura de errores.
while True:
    try:
        num=int(input("Escriba un número de 3 dígitos: "))
        if -1000<num<-99 or 99<num<1000:
        #Sí el número es entero de tres cifras.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")
    
if det_si_dig1(num):
#Sí el número contiene el dígito 1
    print("\nEl número contiene el dígito 1.")
else: 
    print("\nEl número no contiene el dígito 1.")
