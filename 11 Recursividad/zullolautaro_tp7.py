"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""
def calcular_factorial(numero):
  if numero == 0:
    return 1
  else:
    return numero * calcular_factorial(numero - 1)

numero_usuario = int(input("Ingresa un número entero: "))
print(f"Factorial: {calcular_factorial(numero_usuario)}")

"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""
asd = 0
def fibonacci(pos):
  if pos <= 0:
    return 0
  elif pos == 1:
    return 1
  else:
    return fibonacci(pos - 1) + fibonacci(pos - 2)

numero_usuario = int(input("Ingresa un número entero: "))
for i in range(numero_usuario):
  print(f"Sucesion de fibonacci: {fibonacci(i)}")
print(f"Resultado funal de fibonacci: {fibonacci(numero_usuario)}")

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un
algoritmo general.
"""
def calcular_potencia(base, exp):
  if exp == 0:
    return 1
  else:
    return base * calcular_potencia(base, exp - 1)

calcular_potencia(7, 5)

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""
def decimal_a_binario(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return str(decimal_a_binario(num // 2)) + str(num % 2)

decimal_a_binario(10)

"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""
def es_palindromo(palabra):
  if len(palabra) <= 1:
    return True
  elif palabra[0] != palabra[-1]:
    return False
  else:
    return es_palindromo(palabra[1:-1])

es_palindromo("oso")

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4)
suma_digitos(9)      → 9
suma_digitos(305)    → 8   (3 + 0 + 5)
"""
def suma_digitos(n):
  if (n < 10):
    return n
  else:
    return n % 10 + suma_digitos(n // 10)

suma_digitos(150)

"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.

Ejemplos:
contar_bloques(1)   → 1         (1)
contar_bloques(2)   → 3         (2 + 1)
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
"""
def contar_bloques(n):
  if n == 0:
    return 0
  else:
    return n + contar_bloques(n - 1)

print(contar_bloques(4))

"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
      Ejemplos:
contar_digito(12233421, 2)   → 3
contar_digito(5555, 5)       → 4
contar_digito(123456, 7)     → 0
"""
def contar_digito(numero, digito, contador=0):
  if numero == 0:
    return contador
  else:
    if numero % 10 == digito:
      contador += 1
    return contar_digito(numero // 10, digito, contador)

print(f"Cantidad de veces que aparece: {contar_digito(5555, 5)}")