class Tablero:
    def __init__(self, list1, list2, list3, list4):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4

    def movimiento(self, letra, direccion):
        if letra  in self.list1:
            pos = self.list1.index(letra)
            if direccion == "derecha" and self.list1[pos+1] == "":
                espacio = self.list1[pos+1]
                self.list1[pos+1] = letra
                self.list1[pos] = espacio
            if direccion == "izquierda" and self.list2[pos-1] == "":
                espacio = self.list1[pos-1]
                self.list1[pos-1] = letra
                self.list1[pos] = espacio
            if direccion == "abajo" and self.list2[pos] == "":
                espacio = self.list2[pos]
                self.list2[pos] = letra
                self.list1[pos] = espacio
            if direccion == "arriba":
                print("El movimiento no es posible")
            return self.list1, self.list2
        elif letra  in self.list2:
            pos = self.list2.index(letra)
            if direccion == "derecha":
                espacio = self.list2[pos+1]
                self.list2[pos+1] = letra
                self.list2[pos] = espacio
            if direccion == "izquierda":
                espacio = self.list2[pos-1]
                self.list2[pos-1] = letra
                self.list2[pos] = espacio
            if direccion == "abajo" and and self.list3[pos] == "":
                espacio = self.list3[pos]
                self.list3[pos] = letra
                self.list2[pos] = espacio
            if direccion == "arriba":
                espacio = self.list1[pos]
                self.list1[pos] = letra
                self.list2[pos] = espacio
            return self.list1, self.list2, self.list3
        elif letra  in self.list3:
            pos = self.list3.index(letra)
            if direccion == "derecha":
                espacio = self.list3[pos+1]
                self.list3[pos+1] = letra
                self.list3[pos] = espacio
            if direccion == "izquierda":
                espacio = self.list3[pos-1]
                self.list3[pos-1] = letra
                self.list3[pos] = espacio
            if direccion == "abajo":
                espacio = self.list4[pos]
                self.list4[pos] = letra
                self.list3[pos] = espacio
            if direccion == "arriba":
                espacio = self.list2[pos]
                self.list2[pos] = letra
                self.list3[pos] = espacio
            return pos
        elif letra  in self.list4:
            pos = self.list4.index(letra)
            if direccion == "derecha":
                espacio = self.list4[pos+1]
                self.list4[pos+1] = letra
                self.list4[pos] = espacio
            if direccion == "izquierda":
                espacio = self.list4[pos-1]
                self.list4[pos-1] = letra
                self.list4[pos] = espacio
            if direccion == "abajo":
                print("Este movimiento no es posible")
            if direccion == "arriba":
                espacio = self.list3[pos]
                self.list3[pos] = letra
                self.list4[pos] = espacio
            return pos
    

    
    




l1=["A","","C"] 
l2=["D","E","F"]
l3=["G","H","I"]
l4=["J","K","L"]
t = Tablero(l1, l2, l3, l4)
p = t.movimiento("C","abajo")
print(p)