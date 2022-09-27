'''

Actividad: Para saber si un año es bisiesto o no
'''

year = int(input("Introduce un año:"))

if year % 4 != 0: #No es divisible entre 4
    print('Año comun')
elif year % 100 != 0: #año bisiesto
     print('Año bisisesto')
elif year % 400 != 0:
    print('Año Comun')
else:
    print('De lo contrario, es un año bisiesto')


