'''
Autor:Edgar Francisco Hernandez Mendez
Fecha: 27/09/22
Actividad: "Utilizar la sentencia if-else para ramificar la ruta de control"
'''

income = float(input("Introduce el ingreso anual:"))

tax = 0
if income < 85528 :
    tax = income * 0.18 - 556.02
else:
    tax = 14,839.2 + (income - 85,528 ) * 0.32 


tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
