"""
ZulloLautaro_TP4
"""

"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""

for i in range(101):
  print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

numero = int(input("Ingrese un numero: "))
contador = 0

while numero >= -1:
  if (numero == 0):
    contador += 1
    break
  numero //= 10
  print(numero)
  contador += 1
  numero -= 1

print(f"Cantidad de digitos: {contador}")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
sum = 0
for i in range(num1 + 1, num2):
  sum += i

print(f"Suma: {sum}")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

num = 1
sum = 0
while num != 0:
  num = int(input("Ingrese un numero (0 para salir): "))
  sum += num

print(f"Sumatoria: {sum}")

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random

numero_correcto = random.randint(0, 9)
numero = int(input("Ingrese un numero: "))
intentos = 1

while numero != numero_correcto:
  numero = int(input("Ingrese otro numero: "))
  intentos += 1

print(f"Ganaste en {intentos} intento/s")

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""

i = 100
while i >= 0:
  print(i)
  i -= 1

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

num1 = int(input("Ingrese un numero entero positivo: "))
if num1 > 0:
  sum = 0
  for i in range(0, num1):
    sum += i
  print(f"Suma: {sum}")
else:
  print("El numero tiene que ser entero positivo")

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

par = 0
impar = 0
positivo = 0
negativo = 0
cero = 0

for i in range(100):
  num = int(input("Ingrese numero: "))

  if num % 2 == 0:
    par += 1
  else:
    impar += 1

  if num > 0:
    positivo += 1
  elif num < 0:
    negativo += 1
  else:
    cero += 1

print(f"""
Estadisticas:
  - Numeros pares: {par}
  - Numeros impares: {impar}
  - Numeros positivos: {positivo}
  - Numeros negativos: {negativo}
  - Ceros ingresados: {cero}
""")

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

rango = 100
sum = 0

for i in range(rango):
  num = int(input("Ingrese numero: "))
  sum += num

print(f"Media: {sum / rango}")

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingrese un numero: "))
resultado = ""

while numero != 0:
  resultado += str(numero % 10)
  numero //= 10


print(f"Cantidad de digitos: {resultado}")