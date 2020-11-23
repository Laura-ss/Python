#cadena = input("Escribe lo que quieras:")
#subcadena = ""

#for i in cadena.split():
 #   if subcadena.find(i) >= 0:
  #      print (i, "está repetida")
   # subcadena = subcadena + " " + i

#Si se prueba con el ejemplo "Hola quería decir que no todo es tan sencillo",el programa falla porque confunde el "que" de "quería" con el otro.

##Se añade también para que pueda identificar como repetidas palabras en mayúsculas y minúsculas que sean iguales

cadena = input("Escribe lo que quieras:")
subcadena = ""

for i in cadena.split():
    if subcadena.lower()find("^" + i.lower() + "^") >= 0:
        print (i, "está repetida")
    subcadena = subcadena + "^" + i + "^"
    print (subcadena)