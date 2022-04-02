# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:23:18 2019

@author: Nicolas
"""
#Este programa lee un número entero y calcula la suma de los números múltiplos 
#de 3  desde 0 hasta el número, utilizando: ciclo para, ciclo mientras,
#ciclo repita hasta que.

#Esta función determina si el número 'num' es múltiplo del número 'dig'.
def es_mult_dig(num, dig):
    num=abs(num)
    return (num%dig==0)
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
        
#a) Utilizando ciclo para: 
suma=0
for i in range (0, abs(num)):
    if es_mult_dig((i+1), 3):
    #Sí el número 'i+3' es múltiplo de 3.
        suma+=(i+1)
if num<0:
    suma=(suma*(-1))
    #Sí el número es negativo la suma de los número múltiplos de 3
    #será negativa.
print(f"a) La suma de los números múltiplos de 3, desde cero hasta el número \
ingresado, es {suma}.")

#b) Utilizando ciclo mientras:
suma=0
cont=1
while cont<=abs(num):
#Mientras no se hayan evaluado todos los números anteriores al número 'num'.
    if es_mult_dig(cont, 3):
        suma+=cont
    cont+=1
if num<0:
    suma=(suma*(-1))
    #Sí el número es negativo la suma de los número múltiplos de 3
    #será negativa.
print(f"b) La suma de los números múltiplos de 3, desde cero hasta el número \
ingresado, es {suma}.")

#c) Utilizando ciclo repita-hasta:
suma=0
cont=0
while True:                                 
    if es_mult_dig(cont, 3):
        suma+=cont
    if cont>=abs(num):
    #Sí se han evaluado todos los números hasta el número de interes.
        break
    cont+=1
if num<0:
    suma=(suma*(-1))
    #Sí el número es negativo la suma de los número múltiplos de 3
    #será negativa.
print(f"c) La suma de los números múltiplos de 3, desde cero hasta el número \
ingresado, es {suma}.")