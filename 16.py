# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:45:01 2019
@author: Nicolas
"""
#Este programa lee una cadena de texto e informa al usuario cuales son 
#las palabras más largas y mas cortas en dicho texto.

#Esta función recibe una cadena de texto y devuelve la palabra más larga.
def mayor_palabra(txt):
    palabra=''
    acumula=''
    mayor=''
    #Se crea 'mayor' con cero caracteres de modo que cualquier palabra 
    #sea mayor a 'mayor'.
    n=int(len(txt))
    for j in range (0, n):
        if txt[j]!=' ':
            palabra+=txt[j]
            if j==(n-1):
            #Cuando llega al último caracter, o sea, cuando termina la última
            #palabra.
                if int(len(palabra))>int(len(mayor)):
                    mayor=palabra    
                    acumula=''
                    #Borra lo almacenado en acumula, porque se encontró una 
                    #palabra más larga.
                    acumula+=palabra+' '
                elif int(len(palabra))==int(len(mayor)):
                    acumula+=palabra+' '
            
        else: 
        #Cuando hay un espacio, o sea, cuando termina una palabra.
         #Pueden ocurrir dos eventos, que sea mayor o que sea igual.
            if int(len(palabra))>int(len(mayor)):
                mayor=palabra    
                acumula=''
                #Borra lo almacenado en acumula, porque se encontró una 
                #palabra más larga.
                acumula+=palabra+' '
            elif int(len(palabra))==int(len(mayor)):
                acumula+=palabra+' '
            #Sí la palabra actual es mayor que la almacenada, se cambia.
                mayor=palabra 
            palabra=''
            #Se borra lo que hay en 'palabra' para formar una nueva en el ciclo 
            #siguiente.
    return (acumula)

#La función recibe una cadena de texto y devuelve la palabra más corta.
def menor_palabra(txt):
    palabra=''
    acumula=''
    menor='___________________________________________________________________\
______________________________________________________________________________'
    #Se crea 'menor' con muchos caracteres de modo que cualquier palabra normal
    #sea menor a 'menor'.
    n=int(len(txt))
    for j in range (0, n): 
        if txt[j]!=' ':
            palabra+=txt[j]
            if j==(n-1): 
            #Cuando llega al último caracter, o sea, cuando termina la última
            #palabra.
                if len(palabra)<len(menor): 
                    menor=palabra    
                    acumula=''
                    #Borra lo almacenado en acumula, porque se encontró una 
                    #palabra más larga.
                    acumula+=palabra+' '
                elif len(palabra)==len(menor):
                    acumula+=palabra+' '
        else: 
        #Cuando hay un espacio, o sea, cuando termina una palabra.
        #Pueden ocurrir dos eventos, que sea mayor o que sea igual.
            if len(palabra)<(len(menor)):
                menor=palabra    
                acumula=''
                #Borra lo almacenado en acumula, porque se encontró una 
                #palabra más larga.
                acumula+= palabra+' '
            elif int(len(palabra))==int(len(menor)):
                acumula+=palabra+' '
                #Sí la palabra actual es mayor que la almacenada, se cambia.
                menor=palabra 
            palabra=''
            #Se borra lo que hay en 'palabra' para formar una nueva en el ciclo 
            #siguiente.
    return (acumula)

#La función determina el número de espacios  y retorna 's' si hay 
#más de una palabra.
def num_spacs_plur_sing(txt):
    cont=0
    for i in range(0, len(txt)):
        if txt[i].isspace():
        #Se utiliza el comando .isspace() para evaluar cada caracter.
            cont+=1
    if cont!=1:
        return 's'
    else:
        return ''
#Esta función determina si los caracteres de una frase son alfabéticos, es
#decir si todas las combinaciones de caracteres son palabras.
def is_alpha_frase(txt):
    palabra=''
    aux=0
    numpal=0
    for j in range (0, len(txt)):
    #Para que se evaluen todos los caracteres, el número de ciclos es igual 
    #al número de caracteres.
        if txt[j]!=' ':
        #Para evaluar sí la combinación de caracteres pertenece al alfabeto, es
        #necesario quitar los espacios entre palabras.
            palabra+=txt[j]
            #Se forma catracter a caracter la palabra.
            if j==(len(txt)-1):  
            #Cuando se encuentre en el último caracter es porque esa palabra ha 
            #terminado.
                numpal+=1
                if palabra.isalpha():
                    aux+=1
        else:   
        #Cuando haya un espacio es porque se ha terminado la palabra actual.                               
            numpal+=1
            if palabra.isalpha():
                aux+=1
            palabra=''
            #Se reinicia la variable que recibe la palabra para comenzar a 
            #construir una nueva.
    return (aux==numpal)
    #Sí el número de palabras es igual al número almacenado en 'aux' es porque
    #todas las combinaciones de caracteres del texto introducido son palabras.
    
#Captura de errores.
while True:
    try:
        txt=input(str("Escriba algunas palabras: "))
        if is_alpha_frase(txt):
        #Sí todas las combinaciones de caracteres son palabras.
            break
        print("\n\aVuelva a intentarlo")
    except:
        print("\n\aVuelva a intentarlo")
        
Menores =(menor_palabra(txt)).replace(' ', ', ')
Mayores =(mayor_palabra(txt)).replace(' ', ', ')
#Para que al imprimir, las pabras queden separadas y se puedan diferenciar.

print(f"La{num_spacs_plur_sing(menor_palabra(txt))} \
palabra{num_spacs_plur_sing(menor_palabra(txt))} más \
corta{num_spacs_plur_sing(menor_palabra(txt))}:\n\u2981 \
\"{Menores}\b\b\".\nLa{num_spacs_plur_sing(mayor_palabra(txt))} \
palabra{num_spacs_plur_sing(mayor_palabra(txt))} más \
larga{num_spacs_plur_sing(mayor_palabra(txt))}:\n\u2981 \
\"{Mayores}\b\b\".")
#Los comandos '\b\b' se utilizan para borrar los últimos dos caracteres', ' que
#genera el 'replace'.
