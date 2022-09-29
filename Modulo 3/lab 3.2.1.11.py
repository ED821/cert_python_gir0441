'''
Autor:Edgar Francisco Henandez Mendez
Fecha:29/09/2022
Actividad:Imprimir la palabra asignada a word_without_vowels.

'''


palabraSinVocal  =  ""
palabrausuario  =  ""

userWord  =  input ( "Ingrese una palabra: " )
palabrausuario  =  palabrausuario . superior ()

for  letra  in  userWord :
    if  letra  ==  "A" :
        continue
    elif  letra  ==  "E" :
        continue
    elif  letra  ==  "yo" :
        continue
    elif  letra  ==  "O" :
        continue
    elif  letra  ==  "U" :
        continue
    
    else :
        palabraSinVocal  +=  letra

print(palabraSinVocal )