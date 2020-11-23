solicitar_lista = input("Escribe la lista de números")
lista = []

for número in solicitar_lista.split():
    número = float(número)
    lista.append(número)

print ("La suma es:",sum(lista),",","la media es:",sum(lista)/len(lista))
print (lista)
lista_ordenada = lista

#Es una orden, no se puede guardar en una variable
lista_ordenada.sort()
print(lista_ordenada)

if len(lista) % 2 ==1:
    print("Mediana:", lista_ordenada[len(lista_ordenada)//2])
else:
    temp = (lista_ordenada[len(lista_ordenada)//2 - 1] + lista_ordenada[len(lista_ordenada)//2]) /2
    print("Mediana:", temp)


    