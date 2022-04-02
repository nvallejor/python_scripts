# -*- coding: utf-8 -*-
"""
Created on Sat May 18 07:02:21 2019

@author: Nicolas
"""
#Este programa lee las coordenadas (x1,y1,r1) y (x2,y2,r2) 
#que corresponden al centro y al radio de dos círculos. Posteriormente lee las
#coordenadas de un punto (a,b) y determina si (a,b) está contenido dentro
#del circulo 1, dentro del círculo 2 o dentro de ambos círculos.

#Esta función determina si el punto (a,b) está en el círculo de centro (x,y)
#y radio 'r'.
def det_pto_E_circu(a, b, x, y, r):
    import math
    return((math.sqrt((a-x)**2)+((b-y)**2))<=r)
    #Sí el punto está en el círculo, entonces la distancia entre el centro del
    #círculo y el punto debe ser menor o igual al radio.
    #La distancia entre el centro del círculo y el punto, se haya con la
    #fórmula de distancia entre dos puntos para el plano cartesiano.
  
#Captura de errores.
while True:
    try:
        x1, y1, r1=int(input("\u25cfIngrese la primera coordenada \
del centro del primer círculo: ")),  int(input("\u25cfIngrese la segunda \
coordenada del centro del primer círculo: ", )), int(input("\u25cfIngrese \
el radio del primer círculo:  "))
        x2, y2, r2=int(input("\u25cbIngrese la primera coordenada \
del centro del segundo círculo: ", )), int(input("\u25cbIngrese la segunda \
coordenada del centro del segundo círculo: ", )), int(input("\u25cbIngrese el \
radio del segundo círculo: "))
        a, b=int(input("\u279bIngrese la primera coordenada del \
punto: ")),int(input("\u279bIngrese la segunda coordenada del punto: "))
        if r1>0 and r2>0:
        #Para tener un círculo, el radio debe ser mayor que cero.
            break  
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")
        
if det_pto_E_circu(a, b, x1, y1, r1) and  det_pto_E_circu(a, b, x2, y2, r2):
    print(f"El punto ({a},{b}) se encuentra en el circulo 1\
 (Centro= ({x1},{y1}), Radio= {r1}) y en el circulo 2\
 (Centro= ({x2},{y2}), Radio= {r2}).")
elif det_pto_E_circu(a, b, x1, y1, r1):
    print(f"El punto ({a},{b}) se encuentra en el circulo 1\
 (Centro= ({x1},{y1}), Radio= {r1}).")
elif det_pto_E_circu(a, b, x2, y2, r2):
    print(f"El punto ({a},{b}) se encuentra en el circulo 2\
 (Centro= ({x2},{y2}), Radio= {r2}).")
else:
    print(f"El punto ({a},{b}) no se encuentra en alguno de los círculos.")


