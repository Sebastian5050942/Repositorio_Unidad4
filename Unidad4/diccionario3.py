#Diccionario de 3 Métodos

Vehículos = {
    "Mazda" : "CX60",
    "Chevrolet" : "Corvette",
    "Ferrari" : "458 Spyder"
}
Vehículos["Mazda"] = "CX60" 
Vehículos["Chevrolet"] = "Corvette"
Vehículos["Ferrari"] = "458 Spyder"

print(Vehículos)

#Diccionario con método popitem()
Vehículo_eliminado = Vehículos.popitem()
print(f"Vehículo eliminado: {Vehículo_eliminado}")
print(f"Diccionario actualizado: {Vehículos}")

#Diccionario con método keys()
claves = Vehículos.keys()
print(f"Claves del diccionario: {claves}")

