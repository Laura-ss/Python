def potencia(base):
    """Documentación"""
    exponente=1
    while True:
        yield base**exponente
        exponente+=1

i = 0
it = potencia(2)
while i < 100:
    print(it.__next__())
    i += 1
