# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:53:38 2019
@author: Nicolas
"""
#Este programa calcula  la suma de todos los múltiplos de 3 y 5 
#que hay entre 101 y 1001.

#Esta función determina si el número 'num' es múltiplo del número 'dig'.
def es_mult_dig(num, dig):
    num=abs(num)
    return (num%dig==0)
#Esta función retorna la suma de los múltiplos de 'dig1' y 'dig2' desde un 
#número de inicio 'de' hasta otro de final 'a'.
def sum_mutl_digts_de_a(de, a, dig1, dig2):
    suma=0
    for i in range (0, ((a-de)+1)): 
    #Se hacen los ciclos necesarios para garantizar que evalua todos lo números
    #entre los dos números ingresados, incluyendo el límite superior.
        if es_mult_dig((de+i), dig1):
            suma+=(de+i) 
            continue
            #Sí el número es múltiplo del 3, se agraga a suma, si 
            #fuera también múltiplo del 5 (ejemplo 120) no hay necesidad de 
            #volver a agregarlo a la suma.
        if es_mult_dig((de+i), dig2):
            suma+=(de+i)
    return(suma)

print(f"\nLa suma de los números múltiplos de 3 y de 5 desde 101 hasta 1001 es\
 {sum_mutl_digts_de_a(101, 1001, 3, 5)}.")
