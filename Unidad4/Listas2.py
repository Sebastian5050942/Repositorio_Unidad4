canciones = ["Ella", "Borro Cassette", "Amor", "Marlboro Rojo", "Al rojo vivo"]

#Cómo se accede a los elementos de la lista
num = len(canciones)
print(num)

#Recorrer una lista

for cancion in canciones:
    print(cancion)

for variable in range(len(canciones)):
    print(canciones[variable])

#Imprimir las canciones en orden inverso

for i in range(4, -1, -1):
    print(canciones[i])
