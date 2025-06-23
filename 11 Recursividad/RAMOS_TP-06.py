# Práctico 6: Recursividad

# EJERCICIO 1:
# def factorial(num):
#    """Calcula el factorial de un número de forma iterativa."""
#    resultado = 1
#    for i in range(1, num + 1):
#         resultado *= i
#    return resultado

# def factorial_recursivo(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial_recursivo(num - 1)

# limite = int(input("Ingrese un número entero positivo: "))

# print("Factoriales con función recursiva:")
# for i in range(1, limite + 1):
#     print(f"{i}! = {factorial_recursivo(i)}")


# EJERCICIO 2:
# def fibonacci(posicion):
#     """Calcula el número de Fibonacci en una posición dada."""
#     if posicion <= 0:
#         return 0
#     elif posicion == 1:
#         return 1
#     else:
#         return fibonacci(posicion - 1) + fibonacci(posicion - 2)

# limite = int(input("Ingresa hasta qué posición mostrar la serie de Fibonacci: "))

# # Mostrar la serie completa
# print(f"\nSerie de Fibonacci hasta la posición {limite}:")
# for i in range(limite + 1):
#     print(f"F({i}) = {fibonacci(i)}")

# EJERCICIO 3:
# def potencia(base, exponente):
#     """Calcula la potencia de una base elevada a un exponente."""
#     if exponente == 0:
#         return 1
#     elif exponente < 0:
#         return 1 / potencia(base, -exponente)
#     else:
#         return base * potencia(base, exponente - 1)

# print("Calcula la potencia de una base elevada a un exponente de forma recursiva.")
# base = float(input("Ingrese la base (puede ser un número decimal): "))
# exponente = int(input("Ingrese el exponente: "))
# resultado = potencia(base, exponente)
# print(f"{base} elevado a {exponente} es: {resultado}")

# EJERCICIO 4:
# def decimal_a_binario(numero):
#     """Convierte un número decimal a su representación binaria."""
#     if numero == 0:
#         return "0"
#     elif numero == 1:
#         return "1"
#     else:
#         return decimal_a_binario(numero // 2) + str(numero % 2)
    
# numero = int(input("Ingrese un número entero positivo: "))
# if numero < 0:
#     print("Por favor, ingrese un número entero positivo.")
# else:
#     resultado = decimal_a_binario(numero)
#     print(f"La representación en binario de {numero} es: '{resultado}'")

# EJERCICIO 5:
# def es_palindromo(palabra):
#     """Verifica si una palabra es un palíndromo."""
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])

# palabra = input("Ingrese una palabra: ").strip().lower()
# print(es_palindromo(palabra))

# EJERCICIO 6:
# def suma_digitos(numero):
#     """Calcula la suma de los dígitos de un número entero positivo."""
#     if numero == 0:
#         return 0
#     else:
#         return (numero % 10) + suma_digitos(numero // 10)
    
# numero = int(input("Ingrese un número entero positivo: "))
# if numero < 0:
#     print("Por favor, ingrese un número entero positivo.")
# else:
#     resultado = suma_digitos(numero)
#     print(f"La suma de los dígitos de {numero} es: {resultado}")

# EJERCICIO 7:
# def contar_bloques(n):
#     """Calcula el número de bloques necesarios para construir una pirámide de n niveles."""
#     if n == 0:
#         return 0
#     else:
#         return 1 + contar_bloques(n - 1)

# while True:    
#     try:
#         n = int(input("Ingrese un número entero positivo: "))
#         if n < 0:
#             print("Por favor, ingrese un número entero positivo.")
#         else:
#             bloques = contar_bloques(n)
#             print(f"El número de bloques necesarios para construir una pirámide de {n} niveles es: {bloques}")
#             break
#     except ValueError:
#         print("Entrada no válida. Por favor, ingrese un número entero positivo.")

# EJERCICIO 8:
# def contar_digito(numero, digito):
#     """Cuenta cuántas veces aparece un dígito específico en un número entero positivo."""
#     if numero == 0:
#         return 1 if digito == 0 else 0
#     else:
#         return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
# numero = int(input("Ingrese un número entero positivo: "))
# digito = int(input("Ingrese el dígito a contar (0-9): "))

# if numero < 0 or digito < 0 or digito > 9:
#     print("Por favor, ingrese un número entero positivo y un dígito entre 0 y 9.")
# else:
#     resultado = contar_digito(numero, digito)
#     print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")



