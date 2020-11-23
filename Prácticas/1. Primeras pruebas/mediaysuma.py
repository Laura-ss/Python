x = 0
suma = 0
números = 0
while x != "fin":
    y = input("escribe un número: ")
    x=y
    if (y != "fin"):
       x = int(y)
       suma = suma + x
       números += 1
    
   
print(x)
print (suma, suma/números)