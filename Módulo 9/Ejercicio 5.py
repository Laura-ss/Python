
# def palabra_larga (filename):
#     longitud_inicial = 0
#     p_larga = ""
#     try:
#         with open(filename, 'r', encoding = "UTF-8") as f_read:
#             for linea in f_read:
#                 for palabra in linea.split():
#                     if len(palabra) > longitud_inicial:
#                         longitud_inicial = len(palabra)
#                         p_larga = palabra
#     except FileNotFoundError:
#         print("ERROR: File not found")
#     return p_larga

# filename = "Módulo 9/prueba-palabras.txt"
# print (palabra_larga(filename))

#-------------------------------------------
# def numero_lineas (filename):
#     lineas = 0
#     with open(filename, 'r') as f_read:
#         for linea in f_read:
#             lineas+=1
#         return lineas


# filename = "Módulo 9/prueba-palabras.txt"
# print (numero_lineas(filename))

#-------------------------------------------

# def potencia (base=2):
#     exponente = 0
#     while exponente < 50:
#         yield base**exponente
#         exponente+=1


# it = list(potencia())

# with open('Módulo 9/potencias.txt', 'w') as f_write:
#     for i in it:
#         f_write.writelines(str(i) + "\n")


#--------------------------------------


# def potencia (base=2):
#     exponente = 0
#     while exponente < 50:
#         yield base**exponente
#         exponente+=1


# with open('Módulo 9/potencias.txt', 'w') as f_write:
#     for i in potencia():
#         f_write.write(str(i) + "\n")

#--------------------------------------


def tiempo_transcurrido(day,month,year):
    import datetime
    today=datetime.date.today()
    past=datetime.date(year, month,day)
    diferencia=abs(today-past)   #para ponerlo en valor absoluto   #cuando se restan dos fechas, únicamente devuelve los días
    print("Han pasado ",diferencia.days* 24, "horas")

import sys

print(sys.argv)
print(type(sys.argv))
###########################################
sys.argv = ["yo", 2020, 11, 25]    # prueba
###########################################

if len(sys.argv) == 4:
    anio = int(sys.argv[1])
    mes = int(sys.argv[2])
    dia = int(sys.argv[3])
else:
    print("ERROR: este programa necesita 3 argumentos: año, mes, dia")
    exit(1)
 
tiempo_transcurrido(dia, mes, anio)
