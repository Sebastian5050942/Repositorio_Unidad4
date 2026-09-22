import math
def analizar_trayectoria(rumbo_planeado, rumbo_real, umbral_desviacion=5):
    #Crear una lista vacia para los índices
    indices = []
    #Hay que verificar que las listas sean de igual longitud
    if not rumbo_planeado or not rumbo_real:
        return None
    #Recorrer cada elemento, calculamos la diferencia y
    #Comprobamos si es mayor que 5. Si es así, ponemos el índice 
    #Dentro de la lista vacia
    for i in range(len(rumbo_planeado)):
        dif = abs(rumbo_planeado[i] - rumbo_real[i])
        if dif > umbral_desviacion:
            indices.append(i)
    return indices


#Datos de prueba
planeado = [45, 45, 45, 90, 90, 170, 180, 225, 225, 270]
real = [43, 47, 48, 86, 91, 95, 183, 176, 222, 230, 265]

#Probando la función
#desviaciones = analizar_trayectoria(planeado, real, 5)
desviaciones = analizar_trayectoria([12, 45], [24, 67, 8], 5)

if not desviaciones:
    print("No hay desviaciones significativas")

if desviaciones != None:
    print(f"Se detectaron desviaciones significativas en los puntos: {desviaciones}")
else:
    print("Revisar los datos enviados")

    