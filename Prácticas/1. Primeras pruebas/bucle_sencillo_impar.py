x_impar=int (input("Escribe un número:"))
y_impar= int (input("Escribe un número:"))

imprimir_xy_impar = ""

while x_impar<y_impar:
    if x_impar%2 == 0:  #Si es par
        x_impar+=1
    imprimir_xy_impar = imprimir_xy_impar + " " + str(x_impar)
    x_impar+=1

print (imprimir_xy_impar)