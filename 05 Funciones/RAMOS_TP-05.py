# Práctico 5: Funciones

# Ejercicio 1:
# def imprimir_hola_mundo():
#     """
#     Esta función imprime "Hola Mundo" en la consola. """
#     print("Hola Mundo")

# Llamar a la función
# imprimir_hola_mundo()


# Ejercicio 2:
# def saludar_usuario(nombre):
#     """
#     Esta función recibe un nombre como parámetro y devuelve un saludo personalizado."""

#     # Elimina los espacios y deja el nombre con buena presentación: primera letra mayúscula y el resto minúsculas.
#     nombre= nombre.strip().capitalize()

#     return f"¡Hola, {nombre}! Qué bueno verte por acá 😊"

# def pedir_nombre():
#     # Evitás saludos como "Hola, " si el usuario no escribe nada.
#     while True:
#         nombre = input("Ingrese su nombre: ").strip()
#         if nombre:
#             return nombre
#         else:
#             print("El nombre no puede estar vacío.")

# nombre_usuario = pedir_nombre()
# saludo = saludar_usuario(nombre_usuario)
# print(saludo)


#Ejercicio 3:
# def informacion_personal(nombre, apellido, edad, residencia):
#     """
#     Esta función recibe el nombre, apellido, edad y lugar de residencia de una persona y devuelve un mensaje con esa información."""

#     nombre = nombre.strip().capitalize()
#     apellido = apellido.strip().capitalize()
#     residencia = residencia.strip().capitalize()

#     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

# def pedir_edad():
#     """
#     Solicita la edad y se asegura de que sea un número válido."""
#     while True:
#         edad = input("¿Cuántos años tenés?: ").strip()
#         if edad.isdigit():
#             return int(edad)
#         else:
#             print("Por favor, ingresá una edad válida (solo números).")


# # Programa principal
# nombre = input("Ingresá tu nombre: ")
# apellido = input("Ingresá tu apellido: ")
# edad= pedir_edad()
# residencia = input("¿Cuál es tu lugar de residencia?: ")

# informacion = informacion_personal(nombre, apellido, edad, residencia)
# print(informacion)


# Ejercicio 4:
# import math 

# def calcular_area_circulo(radio):
#     """
#     Esta función recibe el radio de un círculo y calcula su área.
#     El área se calcula como pi * radio^2.
#     """
#     # Usamos el módulo math para acceder a la constante pi con mas precisión.
#     return math.pi * radio ** 2

# def calcular_perimetro_circulo(radio):
#     """
#     Esta función recibe el radio de un círculo y calcula su perímetro."""
#     return 2 * math.pi * radio

# def pedir_radio():
#     """
#     Solicita al usuario el radio y se asegura de que sea un número positivo."""
#     while True:
#         try:
#             radio = float(input("Ingrese el radio: "))
#             if radio > 0:
#                 return radio
#             else:
#                 print("El radio debe ser un número positivo.")
#         except ValueError:
#             print("Por favor, ingrese un número válido.")

# # Programa principal 
# radio = pedir_radio()
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El área del círculo es: {area:.2f}")
# print(f"El perímetro del círculo es: {perimetro:.2f}")


# Ejercicio 5:
# def segundos_a_horas(segundos):
#     """
#     Esta función convierte segundos a horas. 
#     Recibe la cantidad de segundos como parámetro y devuelve la cantidad de horas."""
   
#     return segundos / 3600

# def pedir_segundos():
#     """
#     Solicita al usuario la cantidad de segundos y se asegura de que sea un número positivo."""
#     while True:
#         try:
#             segundos = int(input("Ingrese la cantidad de segundos: "))
#             if segundos >= 0:
#                 return segundos
#             else:
#                 print("La cantidad de segundos debe ser un número positivo.")
#         except ValueError:
#             print("Por favor, ingrese un número válido.")

# # Programa principal 
# segundos_ingresados = pedir_segundos()
# horas = segundos_a_horas(segundos_ingresados)
# print(f"{segundos_ingresados} segundos son {horas} horas.")


# Ejercicio 6:
# def tabla_multiplicar(numero):
#     """
#     Muestra la tabla de multiplicar del 1 al 10 para el número dado.
#     """
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")

# def pedir_numero():
#     """
#     Solicita un número entero positivo al usuario."""
#     while True:
#         try:
#             numero = int(input("Ingrese un número: "))
#             if numero >= 0:
#                 return numero
#             else:
#                 print("Por favor, ingrese un número positivo.")
#         except ValueError:
#             print("Por favor, ingrese un número válido.")

# def main():
#     """
#     Función principal que solicita un número y muestra su tabla de multiplicar."""

#     print("¡Bienvenido a la tabla de multiplicar!")
#     numero = pedir_numero()
#     tabla_multiplicar(numero)

# main()



# Ejercicio 7:
# Definimos una funcion que recibe dos numeros como parametros y realiza operaciones basicas.

# def operaciones_basicas(a, b):
#     """
#     Esta función recibe dos números y devuelve su suma, resta, multiplicación y división. Devuelve un mensaje de error si se intenta dividir por cero. 
#     Utilizamos una tupla para devolver los resultados de las operaciones."""

#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0 else "Error: No se puede dividir por cero"
    
#     return suma, resta, multiplicacion, division

# # solicitar al usuario dos números y llama a la función operaciones_basicas.
# print("Calculadora de operaciones básicas")

# try:
#     a = float(input("Ingrese el primer número: "))
#     b = float(input("Ingrese el segundo número: "))

#     resultados = operaciones_basicas(a, b)

#     # Mostramos los resultados a traves de la tupla devuelta por la función
#     print("\nResultados:")
#     print(f"Suma: {resultados[0]}")
#     print(f"Resta: {resultados[1]}")
#     print(f"Multiplicación: {resultados[2]}")
#     print(f"División: {resultados[3]}")

# except ValueError:
#     print("Por favor, ingrese números válidos.")


# Ejercicio 8:
# def calcular_imc(peso, altura):
#     """
#     Esta función recibe el peso y la altura de una persona y calcula su índice de masa corporal (IMC).
#     El IMC se calcula como el peso en kilogramos dividido por la altura en metros al cuadrado.
#     Devuelve el IMC calculado."""

#     if altura <= 0:
#         raise ValueError("La altura debe ser mayor que cero.") # raise detiene la ejecución inmediatamente donde ocurre el error.
#     if peso <= 0:
#         raise ValueError("El peso debe ser mayor que cero.")
#     return peso / (altura ** 2)

# def main():
#     print("Calculá tu índice de masa corporal (IMC)")

#     try:
#         peso = float(input("Ingrese su peso en kilogramos: "))
#         altura = float(input("Ingrese su altura en metros: "))

#         imc = calcular_imc(peso, altura)

#         print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#     except ValueError:
#         print(f"Error: Debes ingresar un número válido.")

# main()



# Ejercicio 9:
# def celsius_a_fahrenheit(celsius):
#     """
#     Esta función convierte grados Celsius a Fahrenheit.
#     La fórmula de conversión es: F = (C * 9/5) + 32. 
#     Recibe la temperatura en Celsius como parámetro y devuelve la temperatura en Fahrenheit.
#     """
#     return (celsius * 9/5) + 32

# def main():
#     """
#     Función principal que solicita al usuario una temperatura en Celsius y llama a la función celsius_a_fahrenheit.
#     Muestra el resultado en pantalla.
#     """
#     print("Conversor de Celsius a Fahrenheit")

#     try:
#         celsius = float(input("Ingrese la temperatura en grados Celsius: "))
#         fahrenheit = celsius_a_fahrenheit(celsius)
#         print(f"{celsius}°C son {fahrenheit:.2f}°F")
#     except ValueError:
#         print("Por favor, ingrese un número válido.")

# main()


# Ejercicio 10:
# def calcular_promedio(a, b, c):
#     """
#     Esta función recibe tres números y devuelve su promedio.
#     El promedio se calcula sumando los números y dividiendo por la cantidad de números.
#     """
#     return (a + b + c) / 3

# def pedir_numero(mensaje):
#     while True:
#         try:
#             return float(input(mensaje))
#         except ValueError:
#             print("Por favor, ingrese un número válido.")

# def main():
#     """
#     Función principal que solicita al usuario tres números y llama a la función calcular_promedio y muestra el resultado en pantalla."""

#     print("Calculá tu promedio")

#     a = pedir_numero("Ingrese el primer número: ")
#     b = pedir_numero("Ingrese el segundo número: ")
#     c = pedir_numero("Ingrese el tercer número: ")

#     promedio = calcular_promedio(a, b, c)
#     print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}") 

# main()