"""
1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
"""
print("Hola mundo!")

"""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
"""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y soy de {residencia}")

"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""

radio = int(input("Ingrese radio de circulo: "))

area = 3.14 * (radio * radio)
perimetro = 2 * 3.14 * radio

print(f"El area es {area} y el perimetro es {perimetro}")

"""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""

segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos}s equivale a {horas}hs")

"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""

numero = int(input("Ingrese un numero: "))

for n in range(11):
  if n >= 1:
    print(f"{numero} x {n} = {numero * n}")

"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""

num1 = int(input("Ingrese un numero distinto de 0: "))
num2 = int(input("Ingrese otro numero distinto de 0: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"""
      Suma: {suma}
      Resta: {resta}
      Miltiplicacion: {multiplicacion}
      Division: {division}
""")

"""
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal
"""

altura = float(input("Ingrese su altura en m: "))
peso = float(input("Ingrese su peso en kg: "))

print(f"Su IMC es de: {peso / (altura ** 2)}")

"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit
"""

temperatura = float(input("Ingrese temperatura en celsius: "))

print(f"{temperatura}° celsius son {(9/5) * temperatura + 32}° fahrenheit")

"""
10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de
dichos números.
"""

numero = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))
numero3 = int(input("Ingrese numero: "))

print(f"Promedio: {(numero + numero2 + numero3)/ 3}")