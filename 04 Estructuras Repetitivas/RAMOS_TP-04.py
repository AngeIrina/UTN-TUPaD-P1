# Práctico 4: Estructuras repetitivas

# EJERCICIO 1:
#for n in range(0, 101):
    #print(n)


# EJERCICIO 2:
#num = int(input("Ingrese un número entero: "))
#cant_digitos = len(str(abs(num)))  # Convertir el número a cadena y contar los dígitos, abs() se encarga del signo.
#print(f"El número {num} tiene {cant_digitos} dígitos.")


# EJERCICIO 3:
#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número: "))

# Evita errores si el usuario escribe los números en cualquier orden.
#inicio = min(num1, num2)
#fin = max(num1, num2)

#suma = 0
#for i in range(inicio, fin + 1):
    #suma += i

#print(f"La suma de los números enteros entre {num1} y {num2} es: {suma}")


# EJERCICIO 4:
#total = 0
#num = int(input("Ingrese un número entero positivo (0 para terminar): "))
#while num != 0:
    #if num < 0:
        #print("No se permiten números negativos. Intente nuevamente.")
    #else:
        #total += num
    #num = int(input("Ingrese otro número (0 para terminar): "))

#print("Ingresó el número 0, se terminó el programa.")    
#print(f"La suma de los números que ingresó es: {total}")


# EJERCICIO 5:
#import random 

#intentos = 0
#numero_secreto = random.randint(0,9)

#print("Estoy pensando un número entre el 0 y 9. ¡ADIVINA CUÁL ES!")

#num = -1  # Valor inicial para entrar al while

# while num != numero_secreto:
#     num = int(input("Ingresá un número: "))
#     if 0 <= num <= 9:
#         intentos += 1
#         if num < numero_secreto:
#             print("El número es mayor. Probá con otro.")
#         elif num > numero_secreto:
#             print("El número es menor. Probá con otro.")
#     else:
#         print("Por favor ingresá un número entre 0 y 9.")

# print(f"¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intentos.")


# EJERCICIO 6:
#for i in range(100, -1, -2):
#    print(i)


# EJERCICIO 7:
# suma = 0
# num = int(input("Ingrese un número entero positivo: "))

# if num >= 0: 
#     for i in range(0, num + 1):
#         suma += i       
# else:
#     print("El número ingresado no es positivo.") 

# print(f"La suma de los números enteros desde 0 hasta {num} es: {suma}")


# EJERCICIO 8:
# pares = 0
# impares = 0
# negativos = 0
# positivos = 0

# for i in range(1,101):
#     num = int(input(f"{i}. Colocá un número: "))

#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1

# print("NÚMEROS PARES:", pares)
# print("NÚMEROS IMPARES:", impares)
# print("NÚMEROS POSITIVOS:", positivos)
# print("NÚMEROS NEGATIVOS:", negativos)


# EJERCICIO 9:
# suma = 0

# for i in range(1, 101):
#     num = int(input(f"{i}. Ingresá un número entero: "))
#     suma += num

# media = suma / 100
# print(f"La media de los 100 números ingresados es: {media}")


# EJERCICIO 10:
# num = input("Ingresá un número: ")

# if num[0] == "-": # Verifica si el número es negativo y lo convierte a positivo sacando el signo
#     num = num[1:]

# invertido = ""

# for i in range(len(num) - 1, -1, -1): # Recorre el número al revés
#     invertido += num[i]

# print(f"El número invertido es: {invertido}")



