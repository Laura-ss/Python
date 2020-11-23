def área_circunferencia (r):
    área=3.1416*r**2
    return área

radio = 5
print (área_circunferencia(radio))

def devuelve_palabra_más_larga (lista):
    máx_long = ""
    for palabra in lista:
        if len(palabra) > len(máx_long):
            máx_long = palabra
    return máx_long

lista_palabras = ["hola", "mundo", "Zaragoza"]
print (devuelve_palabra_más_larga(lista_palabras))

def devuelve_longitud (lon):
    longitud = 0
    for palabra in lon:
        longitud=longitud + len(palabra)
    return longitud

lista = ["hola","mundo"]
print (devuelve_longitud(lista))