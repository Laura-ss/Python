número = int (input("Inserta aquí un número:"))
base = int(input("Inserta aquí la base:"))
binario = ""


while número>base:
    if base>=2 and base<=9:
        cociente=número//base
        resto= número % base
        binario = str (resto) + binario
        número = cociente
       
    else:
        print ("Error, vuelva a intentarlo:")
        número = int (input("Inserta aquí un número:"))
        base = int(input("Inserta aquí la base:"))
        

print (cociente, binario, sep="")