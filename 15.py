# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:18:45 2019

@author: Nicolas
"""
#Este programa lee una matriz cuadrada, determina su traza y el promedio de los 
#números en ella contenida.

#Captura de errores.
#Es necesario hacer dos capturas de errores, porque para entrar en los ciclos 
#'for' se debe conocer cuantas iteraciones se van a realizar y el número de 
#iteraciones está dado por el tamaño de la matriz.
while True:
    try: 
        tamaño= int(input("Ingrese el número de filas y columnas \
de la matriz cuadrada: "))
        if type(tamaño)==int and tamaño>1:
            break
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo") 
        
suma=0
traza=0
for i in range(0, tamaño):
    for j in range(0, tamaño):
    #Con los dos ciclos 'for' se entran uno por uno los valores de la matriz.
        while True:
        #Se realiza la segunda captura de errores para cada uno de los 
        #coeficientes de la matriz.
            try:
                aij=int(input(f"Ingrese valor ({i+1},{j+1}): "))
                if type(aij)==int:
                    break
                print("\n\aVuelva a intentarlo")
            except:
                print("\n\aVuelva a intentarlo") 
        suma+=aij
        #Se tiene en cuenta el signo para calcular el promedio.
        if i==j:
        #Cuando aij sea un elemento de la diagonal, se suma a la traza.
            traza+=aij
prom=float(suma/(tamaño**2))
print(f"\nLa traza de la matriz es {traza} y el promedio de sus valores \
es {prom}.")
    