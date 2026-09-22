# Clase 15 de Septiembre / 2026

## Objetos

1. Atributos
2. Métodos

# Actividad 1

## Código VSC: 

```python
# Creamos un objeto (en este caso, un número)
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud)  # 10000
print(elevacion)  # 9500

altitud = "muy alto"
print(altitud)
```

### Prueba de ejecución en la Terminal:
<img width="1022" height="91" alt="image" src="https://github.com/user-attachments/assets/5abab6df-c628-4f3b-9d62-f0cbc0f652eb" />

## Código VSC: 

```python
velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))
```

### Prueba de ejecución en la Terminal:
<img width="1025" height="97" alt="image" src="https://github.com/user-attachments/assets/a17177b5-1659-45e4-b33e-330dca6264f9" />

## Código VSC: 

```python
modelo = "Boeing 747"
print(id(modelo))  # Guardamos el ID original

# Intentamos "modificar" el string
modelo = modelo + "-800"
print(modelo)  # "Boeing 747-800"
print(id(modelo))  # ¡ID diferente! Se creó un nuevo objeto
```

### Prueba de ejecución en la Terminal:
<img width="1043" height="92" alt="image" src="https://github.com/user-attachments/assets/d970610b-62e9-4b25-9c00-5f43b7c9f476" />

## Código VSC: 

```python
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
```

### Prueba de ejecución en la Terminal:
<img width="1003" height="205" alt="image" src="https://github.com/user-attachments/assets/5ec7f37a-6d10-4711-b74d-cb8ef9d6e717" />

# Iteración con Bucles While y For

## Código VSC: 

```python
# Simulando lecturas de altitud cada 10 segundos
altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1

for i in range(len(altitudes)): #range genera los indices
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10

for altitud in altitudes: #accedo directamente a los elementos
      print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
      tiempo += 10
```

# Ejemplo

## Código VSC: 

```python
tiempo = [2 , 4, 34, 67, 145]
presion = [234, 333, 100, 122, 99]

print("Tiempo\tpresion")
print("_"*20)
for i in range(len(tiempo)):
    print(f"{tiempo[i]}\t{presion[i]}")
```

### Prueba de ejecución en la Terminal:
<img width="1030" height="160" alt="image" src="https://github.com/user-attachments/assets/329585c8-228b-4355-9d18-755f4b0fab18" />


# Trabajo en IDLE

<img width="700" height="710" alt="image" src="https://github.com/user-attachments/assets/39b88615-0657-4b77-9ef7-1c1c4d296c32" />

# Realiza el siguiente ejercicio y explica (en tu bitácora) tu respuesta a la pregunta:

## ¿Cómo afecta la mutabilidad a los objetos que se usan como argumentos de una función?

### Solución:

#### Código VSC: 

```python
canciones = ["Ella", "Borro Cassette", "Amor", "Marlboro Rojo", "Al rojo vivo"]

#Cómo se accede a los elementos de la lista
print(canciones[5])

```

### Prueba de ejecución en la Terminal:
<img width="1010" height="468" alt="image" src="https://github.com/user-attachments/assets/28d1bcc2-2489-4ed7-b308-8be4ed677e94" />


# Pregunta de Parcial

## Mutabilidad e Inmutabilidad:

La mutabilidad se refiere a si un objeto puede ser modificado después de su creación.

**Objetos Inmutables**: No pueden ser modificados después de su creación. Si parece que los estamos modificando, en realidad estamos creando nuevos objetos.

- Ejemplos: números (int, float), strings, tuplas, frozensets

**Objetos Mutables**: Pueden ser modificados después de su creación.

- Ejemplos: listas, diccionarios, sets

# Clase 17 de Septiembre / 2026

## Código VSC: 

```python
# Lista vacía
componentes = []

# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Lista con diferentes tipos de datos
datos_vuelo = [202, "Boeing 737", True, 10500.5]

# Listas anidadas
matriz_rotacion = [[56, 33, 57], [78, 13, 21], [17, 99, 1]]

print(componentes[2])
print(matriz_rotacion[1][2])
print(matriz_rotacion[2])

filas = len(matriz_rotacion)
col = len(matriz_rotacion[0])

comp2 = componentes[2:]
print(comp2)


```

### Prueba de ejecución en la Terminal:

<img width="1016" height="279" alt="image" src="https://github.com/user-attachments/assets/c1e7d526-bb27-4f2c-b019-8cf2cb392373" />

## Código VSC: 

```python
# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")

for i in range(len(tiempo)):
    print(f"T+{tiempo[i]}s: Altitud={altitud[i]}m, Velocidad={velocidad[i]}km/h, Fase={est}h, Fase={estado[i]}")
    

```

### Prueba de ejecución en la Terminal:

<img width="1026" height="302" alt="image" src="https://github.com/user-attachments/assets/1b9bc993-f563-423e-8e39-fd35f92c3af2" />

## Código VSC: 

```python
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

```

### Prueba de ejecución en la Terminal:

<img width="995" height="162" alt="image" src="https://github.com/user-attachments/assets/ba3ab206-4eb8-472b-956b-3b295c11c785" />

## Código VSC: 

```python
#Generar una lista de 12 elementos, representando las ventas de celulares al mes de una compañia. Luego encuentre el mes en que más o menos ventas hubo
from random import randint

ventas = []
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for i in range(12):
    ventas.append(randint(200,3000))

print(ventas)
mayor = max(ventas)
pos = ventas.index(mayor)
print(f"Mayor venta ${mayor} en el mes {meses[pos]}")

```

### Prueba de ejecución en la Terminal:

<img width="1015" height="80" alt="image" src="https://github.com/user-attachments/assets/e3d8dd23-3267-4d4a-9390-37220ad5b680" />

# Clase 22 de Septiembre / 2026

## Código VSC: 


```python
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

```

### Prueba de ejecución en la Terminal:

<img width="590" height="152" alt="image" src="https://github.com/user-attachments/assets/7dca68c7-a19a-42cf-a829-c787938d3736" />

## Código VSC: 

```python
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

    

```

### Prueba de ejecución en la Terminal:

<img width="586" height="128" alt="image" src="https://github.com/user-attachments/assets/2244da12-ecb3-484b-9ded-f6c356d985c3" />


