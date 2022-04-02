# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:06:31 2019
@author: Nicolas
"""
#Este programa lee una cadena de texto y la imprime en mayúscula.

#Esta función determina si los caracteres de una frase son alfabéticos.
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


#La función recibe una frase en minúscula y la devuelve en mayúscula.
def frase_a_FRASE(txt):
    frase=''
    for i in range (0, len(txt)):
    #Para que se evaluen todos los caracteres, el número de ciclos es igual 
    #al número de caracteres.
        if txt[i]!=' ':
        #Sí el caracter 'i' no es un espacio se procede a convertirlo a
        #mayúscula.
            if (txt[i]).islower():
                frase+=chr((ord(txt[i]))-32) 
                #Se agrega un caracer a 'frase' que resulta de restarle 32 al 
                #código del caracter 'i' en decimal. Esto es equivalente a 
                #convertir una letra a maýuscula.
            else:  
             #Si el caracter ya está en mayúscula no es necesario convertirlo.
                frase+=txt[i]
        else:
        #Cuando se evalue un espacio, este simplemente se agrega a la frase.
            frase+=' '
    return (frase)
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
        
print(f"\n{frase_a_FRASE(txt)}")
        
                  
     
                


