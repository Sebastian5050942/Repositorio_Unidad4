from random import randint, uniform

#Lista vacia
lista = []

#método append para agregar elementos

dato = randint(0, 100)
lista.append(dato)

#Guardar 10 datos más dentro de la lista
for i in range(10):
    dato = randint(0,100)
    lista.append(dato)
print(lista)

#método remove para quitar elementos
lista.remove(dato)
print(lista)

#Crear dos listas nuevas: la primera va a contener los pares y la segunda los impares
#listas --> 101
#pares --> pares de lista
#impares --> impares de lista
pares = []
impares = []

for dato in lista:
    if dato % 2 == 0:
        pares.append(dato)
    else:
        impares.append(dato)

print("Pares:", pares)
print("Impares:", impares)

#Calular el promedio de lista, pares e impares
#prom_lista
#prom_pares
#prom_impares

suma =+ dato
prom_lista = suma / len(lista)
prom_pares = suma / len(pares)
prom_impares = suma / len(impares)

print(lista)
print(pares)
print(impares)