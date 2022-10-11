'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:11/10/2022
Actividad: El Tremento sat
'''



dinero = int(input("Ingrese la cantidad de dinero: "))

if dinero < 10000 :
    impuesto = dinero*.05+dinero 
    print (impuesto)
if dinero <= 20000:
    impuesto = dinero*.15+dinero
    print (impuesto)
if dinero <= 35000:
    impuesto = dinero*.20+dinero
    print (impuesto)
if dinero <= 60000:
    impuesto = dinero*.30+dinero
    print (impuesto)
if dinero > 60000:
    impuesto = dinero*.45+dinero
    print (impuesto)