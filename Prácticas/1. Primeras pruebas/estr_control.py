x=int(input("Dame un múmero >= 0: "))

hay_error = False
if x < 0:
    print ("Error")
    x = 0
    hay_error = True
else:
    if x == 0:
        print('Zero')
    elif x == 1 or x < 2.0:
        print('Single')

if x == 1:
    print("Es un 1 redondo")
else:
    print('More')

print ("Continuará...y el dato era erróneo:", hay_error)