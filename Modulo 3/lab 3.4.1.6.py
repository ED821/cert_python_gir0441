'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:29/09/2022
Actividad: Usar instrucciones básicas relacionadas con listas.
Crear y modificar listas
'''
listaSombrero = [
    1,
    2,
    3,
    4,
    5,
]  
listaSombrero[2] = int(input("Ingrese un número: "))

del listaSombrero[len(listaSombrero) - 1]

print("Longitud de la lista:", len(listaSombrero))

print(listaSombrero)

