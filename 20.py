# -*- coding: utf-8 -*-
"""
Created on Sun May 19 02:09:22 2019

@author: Nicolas
"""
#Este programa lee una cadena de texto y la imprime como un triángulo.
#Por ejemplo, si la cadena entrada es: "Es una locura odiar a todas las rosas
#porque una te pinchó: renunciar a todos tus sueños porque uno de ellos no se 
#realizó - El Principito", el programa imprime:
#La última cadena queda centrada con respecto a la base del triángulo.
#                    letras   letras acumuladas
#         E             1       1  
#        sun            3       4
#       alocu           5       9
#      raodiar          7      16
#     atodaslas         9      25
#    rosasporque       11      36 
#   unatepinchó:r      13      49
#  enunciaratodost     15      64
# ussueñosporqueuno    17      81
#deellosnoserealizó-   19     100
#   ElPrincipito       12     112


#La función determina el número de líneas completas
#(sin tener en cuenta la base) que tiene el triangulo hecho con el texto 'txt'.
def num_de_lineas_comp(txt):
    numlin=0
    i=1
    while True:
        if (i**2)<=len(txt)<((i+1)**2):     
        #Cuando tenga los suficientes caracteres para formar la línea 'i',                 
        #pero insuficientes para forma la  línea 'i+1';
        #Para formar línea 'i' el número de  caracteres debe estár en el
        #intervalo [sqrt(i),(sqrt(i)+1)**2).
            numlin=i  
            #Cuando la condición se hace verdadera, el número de líneas 
            #completas que se pueden formar es 'i'                                          
            break
        i+=1
        #Para que se evalue si se puede formar la siguiente fila.
    return(numlin)

#Esta función determina el número de caracteres sobrantes, con ayuda del número 
#de líneas que tiene el triangulo.
def num_crcs_cetrar(txt):
    numlin= num_de_lineas_comp(txt)
    numcrcs= len(txt)-(numlin**2)
    #En el triangulo de pascal el número de caracteres acumulados hasta 
    #la fila 'numlin' corresponde a la expresión 'numlin**2'.
    #El npumero de caracteres sobrantes es la diferencia entre los caracteres
    #totales y los necesarios para formar la línea 'numlin'.
    return (numcrcs)
    #Retorna el número de caracteres que sobran.

#La función devuelve el texto que se debe inprimir en la línea 'lin'.
def lin_num(txt, lin):
    inf=((lin-1)**2)  
    #Para el límite inferior del slicing se tiene en cuenta que hasta la línea
    #'lin' se deben haber usado ((lin-1)**2) caracteres tomando el primer
    #caracter como el número 0.
    sup=inf+((2*(lin-1))+1)
    #EL limite superior del slicing es:
    #('límite inferior'+'número de caracteres que tiene la línea 'lin' +1')
    #El número de caracteres en la línea n está dado por la formula (2(n-1)+1).
    txtlin=txt[inf:sup]
    #El slicing arrojará los caracteres a imprimir en la línea 'lin'.
    return(txtlin)

#La función recibe el número de caracteres'num' de la última línea y 
#devuelve el texto que se debe inprimir en dicha línea.
def last_line(txt, num):
    inf=len(txt)-num
    sup=len(txt)
    lastline=txt[inf:sup]
    return(lastline)
    #Retorna lo que debe imprimirse en la última línea (base).
    
txt1= input(str("Escriba algunas palabras: "))
txt=txt1.replace(' ', '')
#Se quitan todos los espacios de la frase.
       
numlin=  num_de_lineas_comp(txt)
numcentr= num_crcs_cetrar(txt)
lastline= last_line(txt, numcentr)

print('')
for j in range (0, numlin):
    sps=(' '*(numlin-(j+1)))
#El número de espacios de la primera línea es equivalente al número de líneas
#completas que pueden ser impresas (sin contar la base).A partir de este número
#de espacios de la primera fila se obtienen los de las líneas
#siguientes, restando de a 1; Todo esto para que quede centrado.
    print(f"{sps}{lin_num(txt, (j+1))}")
#Cuando termine de inmprimir filas del triángulo, sigue con la base.
else:
    sps=(' '*(numlin-(len(lastline)//2)-1))
    #Si el número de caracteres sobrantes es impar, la base quedará centrada, 
    #si es par, quedará desfasada por un caracter.
    print(f"{sps}{lastline}")








