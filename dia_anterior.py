"""
Tarea:    día anterior
Autor:    Juan Oablo Rubio
Fecha:    07/abr/21
Grupo:    ESI-232
Profesor: Jorge A. Zaldívar Carrillo
Descripción: Calcula el dia anterior de una fecha dada.
"""
dia = int(input("Intodusca el numero del día: "))
mes = int(input("Intodusca el numero del mes: "))
año = int(input("Intodusca el numero del año: "))

"""dia<1"""
if dia == 1:

    """1,2,4,6,8,9,11"""
    if mes==1 or mes ==2 or mes==4 or mes==6 or mes==8 or mes==9 or mes==11:
        dia = 31
        mes -= 1

    """Febrero, año bisiesto"""
    if mes ==3 and año%4 == 0:
        dia = 29
        mes -= 1

    """3"""
    if mes ==3:
        dia = 28
        mes -= 1


    """5,7,10,11"""
    if mes==5 or mes ==7 or mes==10 or mes==11:
        dia = 30
        mes -= 1
else:
    dia = dia-1
if mes <= 0:
    mes = 12
    año = año -1

print(dia)
print(mes)
print(año)
    
