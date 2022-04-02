# -*- coding: utf-8 -*-
"""
Created on Thu May 16 00:43:17 2019

@author: Nicolas
"""
#Este programa lee dos números enteros y determina si la diferencia 
#entre los dos es un número primo.

#Esta función determina si un número NO es primo.
def det_num_primo(num):
    aux=0
    num=abs(num)
    if num==1 or num==0:
        aux=1
    for i in range (2, num):
        if (num%i)==0:
        #Sí el número tiene divisores exactos, diferentes de 1 y el mismo.
            aux=1
            break    
    return (aux==1)
    #Verdadero sí el número no es primo.
#Captura de errores.
while True:
    try:
        num1=int(input("Escriba el primer número entero: "))
        num2=int(input("Escriba el segundo número entero: "))
        if type(num1)==int and type(num2)==int:
        #Sí ambos números son enteros.
            break
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")

if det_num_primo((num1-num2)):
    #Sí No es un número primo.
    print("\nLa diferencia entre los dos números no es un número primo.")
else:
    print("\nLa diferencia entre los dos números es un número primo.")
    
    
    