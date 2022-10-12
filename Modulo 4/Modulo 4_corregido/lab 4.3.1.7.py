'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:04/10/2022
Actividad:Cuántos días? escribiendo y utilizando tus propias funciones

'''
def isYearLeap(año):
    esBisiesto = False
    divisibleEntre_4 = año % 4
    divisibleEntre_100 = año % 100
    divisibleEntre_400 = año % 400

    if año >= 1582:
        if divisibleEntre_4 != 0:
            esBisiesto = False
        elif divisibleEntre_100 != 0:
            esBisiesto = True
        elif divisibleEntre_400 != 0:
            esBisiesto = False
        else:
            esBisiesto = True
    else:
        esBisiesto = False

    return esBisiesto


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")