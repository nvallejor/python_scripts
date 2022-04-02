# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:48:13 2019
@author: Nicolas
"""
#Este programa recibe una cadena de texto y reporta:
#a) cuántas letras vocales en mayúscula se entraron;
#b) cuántas letras con tilde se entraron (minúsculas y mayúsculas);
#c) cuántos dígitos se entraron,
#d) cuántos espacios se entraron;
#e) cuántas palabras reservadas se entraron.

#Funciones para plurar singular al imprimir.
def sing_plur(num):
    if num!=1:
        return 's'
    else:
        return ''
def sing_plur2(num):
    if num!=1:
        return 'es'
    else:
        return ''
#a)
#Esta función determina si la letra entrada es una vocal.
def Es_vocal(ltr):
    ltr=ltr.upper()
    aux=0
    if (ltr=='A' or ltr=='E' or ltr=='I' or ltr=='O'or ltr=='U' or ltr=='Á' or
        ltr=='É' or ltr=='Í' or ltr=='Ó' or ltr=='Ú' or ltr=='Ü'):
        aux=1
    return(aux==1)
#La función recibe una cadena y determina cuantas vocales en mayúscula tiene.    
def num_vocs_MYS(txt):
    cont=0
    for i in range(0, len(txt)):
     #Para que se evaluen todos los caracteres, el número de ciclos es igual 
     #al número de caracteres.
        if txt[i].isupper() and Es_vocal(txt[i]):
            cont+=1
    return(cont)
    
#b)
#La funció determina si la letra tiene tilde.
def tiene_tilde(ltr):
    aux=0
    ltr=ltr.upper()
    if  ltr=='Á' or ltr=='É' or ltr=='Í' or ltr=='Ó' or ltr=='Ú' or ltr=='Ü':
    #Los acentos posibles en español.
        aux=1
    return(aux==1)
    #Verdadero sí la letra evaluada tiene tilde.
    
#La función determina el número de tildes.
def num_tildes(txt):
    cont=0
    for i in range(0, len(txt)):
    #Para que se evaluen todos los caracteres, el número de ciclos es igual 
    #al número de caracteres.
        if tiene_tilde(txt[i]):
            cont+=1
    return(cont)
#c)
#La funció determina el número de dígitos.
def num_digs(txt):
    cont=0
    for i in range(0, len(txt)):
        if txt[i].isdigit():
        #Se utiliza el comando .isdigit() para evaluar cada caracter.
            cont+=1
    return(cont)
#d)
#La funció determina el número de espacios.
def num_spacs(txt):
    cont=0
    for i in range(0, len(txt)):
        if txt[i].isspace():
        #Se utiliza el comando .isspace() para evaluar cada caracter.
            cont+=1
    return(cont)
#e)
#La funció determina el número de keywords.
def num_keywords(txt):
    palabra=''
    cont=0
    for j in range (0, len(txt)):
        if txt[j]!=' ':
        #Sí el caracter 'j' no es un espacio se procede a concatenarlo para 
        #formar palabra.
            palabra+=txt[j]
            if j==(len(txt)-1): 
            #Cuando se encuentre en el último caracter es porque la última
            #palabra ha terminado.
                import keyword
                if keyword.iskeyword(f"{palabra}"): 
                #Con el comando '.iskeyword' del módulo 'keyword' se evalua 
                #la palabra una vez terminada.
                    cont+=1
        else:
        #Cuando haya un espacio es porque se ha terminado la palabra actual.  
            import keyword
            if keyword.iskeyword(f"{palabra}"):
            #Con el comando '.iskeyword' del módulo 'keyword' se evalua 
            #la palabra una vez terminada.
                cont+=1
            palabra=''
            #Se reinicia la variable que recibe la palabra para comenzar a 
            #construir una nueva.
    return (cont)
    #Retorna el número de palabras reservadas encontradas.

#Se omite la captura de errores porque el programa acapta todo tipo de 
#caracteres.
txt=input("Ingrese una cadena de texto: ")
        
letmayus=num_vocs_MYS(txt)
ltsT=num_tildes(txt)
digs=num_digs(txt)
sps=num_spacs(txt)
rvds=num_keywords(txt)

print("\nRESULTADOS:")
print(f"\u2981 Se encontró {letmayus} letra{sing_plur(letmayus)} \
vocal{sing_plur2(letmayus)} en mayúscula. \n\u2981 \
Se encontró {ltsT} letra{sing_plur(ltsT)} con tilde.\n\u2981 \
Se encontró {digs} dígito{sing_plur(digs)}.\n\u2981 \
Se encontró {sps} espacio{sing_plur(sps)}.\n\u2981 \
Se encontró {rvds} palabra{sing_plur(rvds)} reservada{sing_plur(rvds)}.")
