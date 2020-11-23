#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_temp_spread_from_csv_file(filename, enc="utf-8"):
    """Devuelve d, mi, mx que son el valor numérico del día, su temperatura mínima 
    y su temperatura máxima para el día que tenga la menor diferencia (max-min), de 
    entre los contenidos en el fichero"""
    COL_TEMP_MIN = 3 #COLUMNA TERCERA (EMPEZANDO EN 1)
    COL_TEMP_MAX = 2
    COL_DIA = 1
    try:
        diff_ganadora = 999
        day_gan = 0
        mx_gan = 0
        mn_gan = 0
        with open(filename, "r") as f_read:
            f_read.readline() #descartar cabecera
            days = f_read.readlines()
            for line in f_read:
                line = line.strip()
                l = line.split(",")
                mx = float(l[COL_TEMP_MAX - 1])
                mn = float (l[COL_TEMP_MIN - 1])
                diff_actual =  mx - mn 
                if diff_actual < diff_ganadora:
                    diff_ganadora = diff_actual
                    day_gan = int(l[COL_DIA - 1])
                    mx_gan = mx
                    mn_gan = mn
                    # print(f"Nuevo candidato: ´{day_gan}, {mx_gan}, {mn_gan}")

    except FileNotFoundError:
        print(f"ERROR, el archivo '{filename}' no existe'")
    
    return day_gan, mx_gan, mn_gan 
    


# Nombre del fichero que se usará
flashcard_filename = "Módulo 9/weather.csv" 
dy, mn, mx = min_temp_spread_from_csv_file (flashcard_filename)


# Leer el fichero en cuestión
print(f"El resultado final es: día {dy}, mínima de {mn} ºF, máxima de {mx}, diferencia de {mx-mn} ºF")



