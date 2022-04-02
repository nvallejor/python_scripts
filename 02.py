# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:30:22 2019
@author: Nicolas
"""
#Este programa lee un número entero de seis dígitos y determina si el segundo
#es igual al penúltimo.

#Esta función determina si el segundo dígito es igual al penúltimo.
def det_dig2_igual_penul(num): 
    num=abs(num)  
    a, aux=divmod(num,100000)
    b, aux=divmod(aux, 10000)
    #El peníltimo dígito queda almacenado en b.
    c, aux=divmod(aux, 1000)
    d, aux=divmod(aux, 100)
    e, aux=divmod(aux, 10)
    #El segundo dígito queda almacenado en e.
    if b==e:
        return " "
    else:
        return " no "
#Captura de errores
while True:
    try:
        num=int(input("Escriba un número de 6 dígitos: "))
        if -1000000<num<-99999 or 99999<num<1000000:
        #Sí el número es entero de seis dígitos.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")   
print(f"\nEl segundo dígito{det_dig2_igual_penul(num)}es igual al penúltimo.")