import random

aviones = ["A320" ,"B747","CESSNA-172","A380","STOL701"]
lista_vacia = []

if aviones: #Si la lista contiene elementos
    print("Esta lista contiene elementos")

if not lista_vacia:
    print("Esta lista esta vacia")
else:
    print("La lista está llena")

modelo = input("Ingrese el modelo:")
#Verificar si un elemento se encuentra dentro de la lista
if modelo in aviones:
    print("El avión pertenece a mi coleccón privada.")

#Elegir un elemento de la lista de forma aleatoria
avion = random.choice(aviones)
print(avion)