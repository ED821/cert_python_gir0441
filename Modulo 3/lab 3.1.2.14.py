'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:29/09/2022
Actividad: Ingresar el numero de bloques
'''

bloques = int(input("Ingrese el número de bloques: "))
altura = 0

while bloques > 0:
    longitudNecesariaDelNivel = altura + 1

    if longitudNecesariaDelNivel <= bloques:
        bloques -= longitudNecesariaDelNivel
        altura += 1
    else:
        break

print("La altura de la pirámide:", altura)
print("Sobran:", bloques, "bloque(s).")