# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:19:52 2019
@author: Nicolas
"""
#Este programa lee un número de días y lo convierta a años, meses, semanas 
#y días.

#a) Utilizando comando "divmod".
#Esta función retorna el número de años, meses, semanas y días.
def añs_mss_sem_ds(num):
    años, num=divmod(num, 365)
    meses, num=divmod(num, 30)
    sems, días=divmod(num, 7)
    return (años, meses, sems, días)
#Esta función retorna 's' si num es plural y '' si es singular.
def sing_plur(num):
    if num!=1:
        return 's'
    else:
        return ''
#Captura de errores.
while True:
    try:
        num=int(input("Ingrese el número de días: "))
        if num>-1:
        #El número debe ser entero positivo o cero.
            break  
        print("\n\aVuelva a intentarlo") 
    except:
        print("\n\aVuelva a intentarlo") 
años, meses, sems, días = añs_mss_sem_ds(num)
aux='es' if meses!=1 else ''
#Plural y singular de la palabra meses.

print(f"a) {num} día{sing_plur(num)} es equivalente a\
 {años} año{sing_plur(años)}, {meses} mes{aux},\
 {sems} semana{sing_plur(sems)} y {días} día{sing_plur(días)}.")


#b) Sin utilizar comando "divmod"
#Esta función retorna el número de años, meses, semanas y días.
def añs_mss_sems_ds2(num):
    import math
    años=math.floor(num/365)
    meses=math.floor((num-años*365)/30)
    sems=math.floor(((num-años*365)-meses*30)/7)
    días=(((num-años*365)-meses*30)-sems*7)
    return (años, meses, sems, días)

años, meses, sems, días = añs_mss_sems_ds2(num)
aux='es' if meses!=1 else ''
#Plural y singular de la palabra meses.

print(f"b) {num} día{sing_plur(num)} es equivalente a\
 {años} año{sing_plur(años)}, {meses} mes{aux},\
 {sems} semana{sing_plur(sems)} y {días} día{sing_plur(días)}.")

























