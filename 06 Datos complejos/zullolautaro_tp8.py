"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
solo_frutas = precios_frutas.keys()
print(solo_frutas)

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
contactos = {}
for i in range(0, 6):
  nombre = input("Ingrese nombre contacto: ")
  telefono = input("Ingrese numero de telefono: ")
  contactos[nombre] = telefono

buscar = input("Mostrar contacto: ")
if buscar in contactos:
  print(contactos[buscar])
else:
  print("No existe")

"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""
frase = input("Ingrese una frase: ")
palabras = frase.split()
set_palabras = set()
palabras_repetidas = {}
for i in palabras:
  if i in set_palabras:
    palabras_repetidas[i] += 1
  else:
    set_palabras.add(i)
    palabras_repetidas[i] = 1

print(f"Set de palabras: {set_palabras}")
print(f"Cantidad de veces que se repite cada palabra: {palabras_repetidas}")

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
alumnos = {}
for i in range(0, 3):
  nombre = input("Ingrese nombre de alumno: ")
  nota1 = int(input("Ingrese la primer nota: "))
  nota2 = int(input("Ingrese la segunda nota: "))
  nota3 = int(input("Ingrese la tercer nota: "))

  tupla_nota = (nota1, nota2, nota3)
  alumnos[nombre] = tupla_nota

for alumno in alumnos:
  promedio = 0
  for nota in alumnos[alumno]:
    promedio += nota
  promedio = promedio / len(alumnos[alumno])
  alumnos[alumno] = {
      "Notas": alumnos[alumno],
      "Promedio": promedio
  }
print(alumnos)

"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

set1 = {11093, 11345, 11343, 1202, 1099}
set2 = {11093, 11345, 11344, 1203, 1098}

print(f"Aprobaron ambos examenes: {set1 & set2}")
print(f"Aprobaron un solo examen: {set1 ^ set2}")
print(f"Aprobaron al menos un examen: {set1 | set2}")

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""
frutas = {
    'Banana': 10,
    'Ananá': 15,
    'Melón': 23,
    'Uva': 12
}

producto = input("Ingrese producto a modificar: ")
stock = int(input("Ingrese cantidad de stock: "))

if producto in frutas:
  frutas[producto] += stock
else:
  frutas[producto] = stock

print(frutas)

"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo: Permití consultar qué actividad hay en cierto día y hora.
"""
agenda = {}

def agregar_evento(dia, hora, evento):
    clave = (dia, hora)
    agenda[clave] = evento
    print(f"Evento agregado: {evento} el {dia} a las {hora}")

def consultar_evento(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        print(f"Evento el {dia} a las {hora}: {agenda[clave]}")
    else:
        print(f"No hay eventos agendados para el {dia} a las {hora}")

agregar_evento("Lunes", "09:00", "Reunión con el equipo")
agregar_evento("Martes", "14:00", "Clase de inglés")
agregar_evento("Viernes", "18:30", "Cita con el dentista")

consultar_evento("Lunes", "09:00")
consultar_evento("Martes", "10:00")

print(f"Todos los eventos: \n{agenda}")

"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores
"""
capitales = {
    "Buenos Aires": "Argentina",
    "Brasilia": "Brasil",
    "Montevideo": "Uruguay",
    "Paraguay": "Asuncion",
    "Venezuela": "Caracas"
}

print(capitales)