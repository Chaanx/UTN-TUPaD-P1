#Inicio actividad 1

lista = list(range(4, 100, 4))
print(lista)

#Inicio actividad 2

animales = ("perro", "gato", "oso", "elefante", "mono")
lista_animales = list(animales)
print(lista_animales)
print(type(lista_animales))

#Inicio actividad 3

mis_materias = []
print(mis_materias)

mis_materias.append("matematica")
mis_materias.append("programacion")
mis_materias.append("organizacion")

print(mis_materias)

#Inicio actividad 4


animales = ("perro", "gato", "conejo", "pez")
lista_animales = list(animales)
print(lista_animales)

lista_animales[1] = "loro"
lista_animales[3] = "oso"
print(lista_animales)


#Inicio actividad 5


""" 
El codigo de este ejercicio elimina el numero mas grande de la lista "numeros"

 """

#Inicio actividad 6

lista_5_en_5 = list(range(10,31,5))
posicion_1_y_2 = lista_5_en_5[0:2]
print(posicion_1_y_2)

#Inicio actividad 7

lista_autos = ("sedan", "polo", "suran", "gol")
autos = list(lista_autos)
autos[1] = "megane"
autos[2] = "clio"
print(autos)

#Inicio actividad 8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#Inicio actividad 9

compras = [["pan", "leche",], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#Inicio actividad 10

lista_anidada = [15, True, [25.5, 59.9, 30.6], False]
print(lista_anidada)