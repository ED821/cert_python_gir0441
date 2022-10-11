'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:11/10/22
Actividad:Jugando con listas

'''



materias = ["Probabilidad", "Programacion de Redes", "Servidores 1", "Electronica", "Redes WAN"]
for i in range(len(materias)-1, -1, -1):
    score = float(input("¿Qué nota sacaste " + materias[i] + " ? "))
    if score >= 8:
        materias.pop(i)
print("Tienes que repetir " + str(materias))

