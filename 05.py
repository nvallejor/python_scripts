# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:19:46 2019

@author: Nicolas
"""
#Este programa lee tres números enteros y determina si el penúltimo dígito
#de los tres números es igual.

#Esta función determina el penúltimo dígito de un número.
def det_pen_dig(num):
    num=abs(num)  
    aux=0
    if num<10:
        aux=-1
    for i in range (1,3):
    #Realiza dos ciclos para obtener el penúltimo dígito.
        num, a=divmod(num, 10)
        #En 'a' queda almacenado el penúltimo dígito.
    if aux==-1:
        return(aux)
        #Sí el número tiene sólo una cifra.
    else:
        return (a)
#Captura de errores.
while True:
    try:
        num1=int(input("Escriba el primer número entero: "))
        num2=int(input("Escriba el segundo número entero: "))
        num3=int(input("Escriba el tercer número entero: "))
        if type(num1)==int and type(num2)==int and type(num2)==int:
        #Sí todos los números son enteros.
            break
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")  
if det_pen_dig(num1)==-1 or det_pen_dig(num2)==-1 or det_pen_dig(num3)==-1:
    print("\nAlguno de los números tiene sólo una cifra, el penúltimo dígito \
de los tres números no es igual.")
    #Sí alguno de los números tiene sólo suna cifra.
elif det_pen_dig(num1)==det_pen_dig(num2)==det_pen_dig(num3):
    #Sí el valor retornado por la función es igual para los tres números.
    print(f"\nEl penúltimo dígito de los tres números es igual.")
else:
    #Sí los penúltimos dígitos del número no son iguales.
    print("\nEl penúltimo dígito de los tres números no es igual.")
    
