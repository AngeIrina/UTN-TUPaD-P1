# TRABAJO PRÁCTICO GRUPAL

# Programa para convertir un número decimal a binario y viceversa.
# El programa permite al usuario convertir números entre decimal y binario,
# manejando errores de entrada y asegurando que los números sean válidos.

# from colorama import init, Fore, Style # Importar colorama para dar color a la salida en consola
# init()

# # Función que convierte un número decimal a binario
# def decimal_a_binario(num_decimal):
#     if num_decimal < 0:
#           return Fore.RED + "Error: El número debe ser positivo."  # Validación: no se permiten números negativos
#     return bin(num_decimal)[2:]  # bin() devuelve una cadena como '0b1010', así que se quita el '0b'

# # Función que convierte un número binario (como cadena) a decimal
# def binario_a_decimal(num_binario):
#     if not set(num_binario) <= {'0', '1'}:  # Validar que solo contenga dígitos binarios
#          return Fore.RED + "Error: Solo se permiten los dígitos 0 y 1."
#     return int(num_binario, 2)  # Convierte binario a decimal

# # Función para verificar si una cadena representa un número entero positivo
# def es_entero_positivo(texto):
#     return texto.isdigit()

# # Función que muestra el menú principal
# def mostrar_menu():
#    print(Style.BRIGHT + Fore.CYAN + "\n--- MENÚ DE OPCIONES ---")
#    print(Fore.CYAN + "1. Convertir decimal a binario")
#    print(Fore.CYAN + "2. Convertir binario a decimal")
#    print(Fore.CYAN + "3. Salir")

# # Función principal del programa
# def main():
#     seguir = True  # Controla si el ciclo del menú continúa
#     while seguir:
#         mostrar_menu()
#         op = input("Selecciona una opción (1, 2 o 3): ")

#         if op == '1':
#             # Opción 1: Decimal a binario
#             entrada = input(Fore.YELLOW + "Ingresa un número decimal: ")
#             if es_entero_positivo(entrada):
#                 decimal = int(entrada)
#                 binario = decimal_a_binario(decimal)

#                 print(Fore.GREEN + f"El número {decimal} en binario es: {binario}")
#             else:
#                 print(Fore.RED + "Error: Ingresa un número entero positivo válido.")

#         elif op == '2':
#             # Opción 2: Binario a decimal
#             binario = input(Fore.YELLOW + "Ingresa un número binario: ")
#             resultado = binario_a_decimal(binario)
#             if isinstance(resultado, int):
#                 print(Fore.GREEN + f"El número {binario} en decimal es: {resultado}")
#             else:
#                 print(resultado)  # Muestra el mensaje de error si la entrada no es binaria válida

#         elif op == '3':
#             # Opción 3: Salir del programa
#             seguir = False
#             print(Fore.YELLOW + "Saliste del programa.")

#         else:
#             # Opción inválida
#             print(Fore.RED + "Por favor, selecciona una opción válida.")

# # Llamada principal al programa
# main()


