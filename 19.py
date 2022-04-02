# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:07:32 2019

@author: Nicolas
"""
#Este programa lee dos palabras (pueden estar en mayúscula o minúscula)
#y determina cual está primero en el diccionario. El programa soporta
#letras con tilde, la ñ y la ü.

#Justificación:
#Para el diccionario el orden se rige por el orden del abecedario, 
#según http://www.wikilengua.org/index.php/Ordenaci%C3%B3n_alfab%C3%A9tica
#el orden cuando se tiene letras con acentos es así: 1)u 2)ú 3)ü.
    
#Esta función asigna un orden adecuado a los caracteres con acentos y la ñ
#para que queden en orden alfabético.
def ord2(c):
    if c=='Á':
        ordn=65.5
        #Como el ord('A') es 65 y  el de 'B' es 66, entonces 'Á' debe estár
        #entre estos dos últimos.
    elif c=='É':
        ordn=69.5
    elif c=='Í':
        ordn=73.5
    elif c=='Ó':
        ordn=79.5
    elif c=='Ú':
        ordn=85.5
    elif c=='Ñ':
        #Como el ord('N') es 78 y  el de 'O' es 79, entonces 'Ñ' debe estár
        #entre estos dos últimos.
        ordn=78.5
    elif c=='Ü':
        #Como el ord('Ú') es 85.5 y  el de 'V' es 86, entonces 'Ü' debe estár
        #entre estos dos últimos.
        ordn=85.7
    return(ordn)

#La función determina cuál caracter va primero, soporta carcateres 
#normales y con tildes.
def crct_vs_crct(c1, c2):
    c1=c1.upper()
    c2=c2.upper()
#Existen dos posibilidades, que alguno de los dos caracteres sea  especial
#(que tenga un acento) o que ninguno sea especial.
    if (c1!='Á'and c1!='É'and c1!='Í'and c1!='Ó' and c1!='Ú'and c1!='Ü' and
    c1!='Ñ'and c2!='Á'and c2!='É' and c2!='Í' and c2!='Ó' and c2!='Ú'and
    c2!='Ü'and c2!='Ñ'):
    #Sí ninguno de los caracteres es especial, entonces se usa la función 
    #ord() normal para determinar cúal va primero.
        if ord(c1)<ord(c2):                          
            primero=c1
        elif ord(c2)<ord(c1):
            primero=c2
        else:
        #Cuando son iguales la variable 'primero' almacena 0, más adelante
        #se utilizará este valor.
            primero='0' 
    else: 
        #La otra posibilidad es que haya algún caracter especial entre
        # los caracteres  ingresados.                                             
        #Aparecen 3 posibilidades, que los dos caracteres sean especiales,
        #que el caracter 1 sea especial o que el caracter 2 sea especial.
        if (c1=='Á' or c1=='É' or c1=='Í' or c1=='Ó' or c1=='Ú' or c1=='Ü' or
            c1=='Ñ') and (c2=='Á' or c2=='É' or c2=='Í' or c2=='Ó' or
            c2=='Ú'or c2=='Ü' or c2=='Ñ'):
        #Sí tanto el caracter 1 como el 2 son especiales (están acentuados)
        #entonces se usa la función alternativa ord2() para determinar el orden
        #de los caracteres.
            if ord2(c1)<ord2(c2):  
                primero=c1
            elif ord2(c2)<ord2(c1):
                primero=c2
            else:
            #Cuando son iguales la variable 'primero' almacena 0, más adelante
            #se utilizará este valor.
                primero='0' 

        elif (c1=='Á' or c1=='É' or c1=='Í' or c1=='Ó' or c1=='Ú' or c1=='Ü' or
            c1=='Ñ'): 
        #Sí el caracter 1 es de orden especial, se aplica la función 
        #alternativa ord2() solamente al caracter 1.
            if ord2(c1)<ord(c2):                         
                primero=c1
            elif ord(c2)<ord2(c1):
                primero=c2
        elif (c2=='Á' or c2=='É' or c2=='Í' or c2=='Ó' or c2=='Ú'or c2=='Ü' 
              or c2=='Ñ'):
        #Sí el caracter 2 es de orden especial, se aplica la función 
        #alternativa ord2() solamente al caracter 2.
             if ord(c1)<ord2(c2):                          
                primero=c1
             elif ord2(c2)<ord(c1):
                primero=c2
    return(primero) 
     #Retorna el que está de primero en orden alfabético, será igual a cero
     # en el caso de que ambos caracteres sean iguales.
        
#La función determina que palabra va primero por ordenamiento alfabético.  
def que_plbra_prmro(plbra1, plbra2):
    plbra1=plbra1.upper()
    plbra2=plbra2.upper()
    primera=0
    for i in range ((0), (min(len(plbra1), len(plbra2)))):
    #Se garantiza que se evaluen todos los caracteres de la palabra más corta.
        if crct_vs_crct(plbra1[i], plbra2[i])==plbra1[i]:
        #Sí la función retorna que el caracter que va de primero en orden 
        #alfabético es el caracter 'i' de la primera palabra.
            primera=plbra1
            break
            #Con que un caracter vaya primero que otro, es suficiente para 
            #determinar que palabra va primero.
        elif crct_vs_crct(plbra1[i], plbra2[i])==plbra2[i]:
        #Sí la función retorna que el caracter que va de primero en orden 
        #alfabético es el caracter 'i' de la segunda palabra.
            primera=plbra2
            break
            #Con que un caracter vaya primero que otro, es suficiente para 
            #determinar que palabra va primero.
        elif crct_vs_crct(plbra1[i], plbra2[i])=='0': 
        #Sí la función encuentra que los caracteres son iguales.
            if i==(min(len(plbra1), len(plbra2)))-1:
            #Sí se está evaluando el último caracter de la palabra más corta
            #y se encontró que también es igual, entonces se procede a decidir
            #que palabra va primero de acuerdo a su cantidad de caracteres.
                if len(plbra1)<len(plbra2):
                #En el diccionario, si las palabras son iguales en los 
                #caracteres comparables uno a uno, entonces la palabra más 
                #corta será la que irá primero.
                    primera=plbra1
                elif len(plbra1)>len(plbra2):
                    primera=plbra2
                elif len(plbra1)==len(plbra2):
                    primera='0'
                #Cuando tiene el mismo número de caracteres y todos estos 
                #caracteres son iguales, entonces las palabras son iguales.
    return((primera))
    #Retorna la primera palabra en orden alfabético, sí ambas son exactamente 
    #iguales retorna un cero caracter.
    
#Captura de errores.
while True:
    try:
        plbra1, plbra2=input(str("\nIngrese la primera \
palabra: ")), input(str("\nIngrese la segunda palabra: "))
        if plbra1.isalpha() and plbra2.isalpha():
        #Sí ambas combinaciones de caracteres son palabras.
            break
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")  


primera=que_plbra_prmro(plbra1, plbra2)
primera=primera.lower()
#En el diccionario las palabras aparecen en minúscula.
if primera !='0':
    print(f"\n\nLa primera palabra en orden alfabético es \"{primera}\".")
else:
    print(f"\n\nLas palabras son iguales.")
        
