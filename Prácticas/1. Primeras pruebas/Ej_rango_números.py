inicio = 5
fin = 11
lista = []
salto = 2

while inicio < fin:
    lista = lista + [inicio]
    inicio += salto

print (lista)

# Otra forma de hacerlo while inicio < fin:
   # lista.append(inicio)
    # inicio += salto
