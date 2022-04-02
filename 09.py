# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:33:15 2019
@author: Nicolas
"""
#Este programa lee un número entero y determina el número de cincos que están 
#consecutivos en el número. 

#Esta función determina cuantas veces (times) se repite en un número (num)
#el dígito (dig).
def det_num_dig_consecu(num, dig):
    times=0
    num=abs(num)
    while num != 0:
        num, a=divmod(num, 10) 
        if a==dig==(num%10):
        #Si el dígito actual y siguiente son 5.
            if dig==((num//10)%10):    
             #Si los dos números siguientes al actual son 5.
                times+=1
            else:  
            #Cuando solo el número siguiente al actual sea 5.
                times+=2
    return (times, dig)
#Captura de errores.
while True:
    try:
        num=int(input("Escriba un número entero: "))
        if type(num)==int:
        #Sí el número es de tipo entero.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo") 
        
times, dig=det_num_dig_consecu(num, 5)
print(f"En el número {num} hay {times} cincos consecutivos.")






