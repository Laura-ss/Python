a=float (input("Escriba un número para el valor de a:"))
b=float (input("Escriba un número para el valor de b:"))
c=float (input("Escriba un número para el valor de c:"))

disc = b**2 - 4*a*c

if disc < 0:
    print ("No tiene solucion")
else:
     x1= (-b + (disc)**0.5)/(2*a)
     x2= (-b - (disc)**0.5)/(2*a)
     print ("El resultado de x es:", x1, x2)