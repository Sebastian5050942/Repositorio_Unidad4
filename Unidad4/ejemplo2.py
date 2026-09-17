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