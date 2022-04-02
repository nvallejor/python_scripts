# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:40:42 2019
@author: Nicolas
"""
#Este programa lee una fecha entre Enero 1 de 2000 y Mayo 7 de 2019 y determina
#el número de días desde ese día hasta Enero 1 de 2020; se tienen en cuenta
#los años bisiestos.

#Esta función recibe la fecha y determina si se encuentra en el periodo
#de tiempo especificado.
def si_fecha_vale(día, mes, año):
    if (1999<año<2020):
        if año==2019:
            if mes<6:
                if mes==5:
                #Sí se encuentra exactamente en el mes de mayo de 2019.
                    if día<8:
                    #Sí se encuentra en los primeros 7 días de mayo de 2019.
                        aux=1
                        #La fecha es valida
                    else:
                        aux=0
                        #La fecha no es valida.
                else:
                #Si el mes corresponde a los primeros 4 meses de 2019.
                    aux=1
                    #La fecha es valida.
            else:
            #Si se encuentra en el mes de abríl o en adelante.
                aux=0
                #La fecha no es valida.
        else:
        #Si se encuentra entre el año 2000 y el 2018.
            aux=1
    else:
    #Si se encuentra antes del 2000 o despues del 2020
        aux=0
    return(aux==1)
    #La fecha es valida

#Esta función determina si el número de días ingresado corresponde con el mes
#ingresado.
def si_mes_vale(días, mes, año):
    aux=0
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    #Sí el mes tiene máximo 31 días.
        if días<=31:
            aux=1
            #El número de días es válido para el mes.
    if  mes==4 or mes==6 or mes==9 or mes==11:
    #Sí el mes tiene máximo 30 días.
        if días<=30:
            aux=1
            #El número de días es válido para el mes.
    if mes==2:
    #Los días de febrero dependen de año bisiesto o no.
        if es_mult_dig(año, 4):
        #Sí el año es bisiesto.
            if días<=29:
                aux=1
                #El número de días es válido para el mes.
        else:
        #Sí el año no es bisiesto.
            if días<=28:
                aux=1
                #El número de días es válido para el mes.
    return (aux==1)
    
#Esta función determina si el número 'num' es múltiplo del número 'dig'.
def es_mult_dig(num, dig):
    num=abs(num)
    return (num%dig==0)

#Esta función retorna 's' si num es plural y '' si es singular. 
def sing_plur(num):
    if num!=1:
        return 's'
    else:
        return ''
    
#Esta función recibe la fecha y retorna el número de días que faltan para el año
#siguiente.
def días_al_año_sig(día, mes, año):
    aux=0
    numdías=0
    if es_mult_dig(año, 4):
    #Sí el año es bisiesto.
        aux=1
    if mes==1:
        numdías=0
        #Número de días transcurrido desde el comienzo del año al comienzo del
        #mes.
    elif mes==2:
        numdías=31
    elif mes==3:
        numdías=59+aux
        #En caso de que el año sea bisiesto se le agrega un día a partir de 
        #de febrero.
    elif mes==4:
        numdías=90+aux
    elif mes==5:
        numdías=120+aux
    elif mes==6:
        numdías=151+aux
    elif mes==7:
        numdías=181+aux
    elif mes==8:
        numdías=212+aux
    elif mes==9:
        numdías=243+aux
    elif mes==10:
        numdías=273+aux
    elif mes==11:
        numdías=304+aux
    elif mes==12:
        numdías=334+aux
    numdías+= día
    #Número de días que han transcurrido desde el comienzo del año.
    return((365+aux)-numdías)  
    #Número de días que faltan para a terminar ese año.
    
#Esta función recibe un año de inicio y uno final, hasta el cual se desean
#conocer los días transcurridos
def días_año_año(de, hasta):
    numdías=0
    for i in range(0, (hasta-de)):
    #El número de ciclos es equivalente al número de años transcurridos.
        if es_mult_dig(año+i, 4):
        #Sí el año es bisiesto.
            numdías+=366
        else:
        #Sí el año no es bisiesto.
            numdías+=365
    return(numdías)
    
#Captura de errores
while True:
    print("\nPor favor ingrese una fecha comprendida entre\
 Enero 1 del año 2000 y Mayo 7 del 2019. ")
    try:
        año=int(input("Ingrese el año: "))
        mes=int(input("Ingrese el número del mes: "))
        día=int(input("Ingrese el día: "))
        if (año>0) and (0<mes<13) and (0<día<32):
            if (si_fecha_vale(día, mes, año)) and si_mes_vale(día, mes, año):
            #Sí la fecha se encuentra en el periodo de fechas admitidas y 
            #el número de días corresponde con el mes ingresado
                break
        print("\n\aVuelva a intentarlo") 
    except:
        print("\n\aVuelva a intentarlo") 

#Total de días transcurridos será la suma entre los días que faltan para el
#año siguiente y los días transcurridos del año siguiente a 2020
totaldías=(días_al_año_sig(día, mes, año))+(días_año_año((año+1), 2020))
print(f"\nDesde la fecha ingresada, {día}/{mes}/{año}, hasta el primero de Enero\
 de 2020 hay {totaldías} día{sing_plur(totaldías)}.")         



    















