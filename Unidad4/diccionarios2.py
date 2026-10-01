#Creación del diccionario
vuelo = {
    "aerolinea": "Avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MDE"
}
#Acceso a valores
ciudad_llegada = vuelo["destino"]
print(ciudad_llegada)

#Modificación de un valor existente
vuelo["destino"] = "CLO"
print(vuelo)

#Agregar un nuevo par clave-valor
vuelo["estado"] = "En el aire"
print(vuelo)

#Uso del método `.get()` (Acceso seguro)
Y = vuelo.get ("Piloto", "Piloto no asignado")
print(Y)

#Eliminar un dato (clave y valor)
piloto = vuelo.pop("Piloto", "Piloto no asignado")
print(piloto)