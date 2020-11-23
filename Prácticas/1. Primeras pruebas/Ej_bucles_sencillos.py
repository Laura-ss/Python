i=0
imprimir = ""

while i<11:
    imprimir = imprimir + " " + str(i)
    i+=1

print (imprimir)


x= int (input("Escribe un número:"))
y= int (input("Escribe un número:"))

imprimir_xy = ""

while x<=y:
    imprimir_xy = imprimir_xy + " " + str(x)
    x+=1

print (imprimir_xy)


palabra = input("Escribe lo que sea:")

for l in palabra:
    print (l)