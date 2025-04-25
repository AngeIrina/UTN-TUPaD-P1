# Trabajo Práctico 5.1 - Listas

# Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# numeros_multiplo_4 = list(range(4, 101, 4))
# print("Números múltiplos de 4 del 1 al 100:")
# print(numeros_multiplo_4)


# Ejercicio 2: Crear una lista con cinco elementos y mostrar el penúltimo. 

# colores = ["magenta", "fucsia", "azul", "amarillo", "verde"]
# print("El penúltimo color de la lista es:", colores[-2]) # Usando index negativo


# Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

# flores = [] # Lista vacía

# flores.append("rosa")
# flores.append("margarita")
# flores.append("lirio")

# print("Lista de flores:", flores)


# Ejercicio 4: Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 

# animales = ["perro", "gato", "conejo", "pez"] # Lista original

# animales[1] = "loro" # Reemplazo del segundo elemento
# animales[-1] = "oso" # Reemplazo del último elemento

# print("Lista de animales:", animales) # Imprimir la lista resultante


# Ejercicio 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros) 

# El programa crea una lista llamada "numeros" con cinco elementos.
# Luego, utiliza la función "max" para encontrar el número máximo en la lista y lo elimina con el método "remove".
# Por último, imprime la lista resultante sin el número máximo. Imprimiendo por pantalla [8, 15, 3, 7].


# Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# numeros = list(range(10, 31, 5)) 
# print("Los dos primeros números de la lista son:", numeros[:2]) 


# Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

# autos = ["sedan", "polo", "suran", "gol"] # Lista original

# autos[1] = "peugeot" # Reemplazo del segundo elemento
# autos[2] = "fiat" # Reemplazo del tercer elemento

# print(autos) 


# Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.

# dobles = [] # Lista vacía

# dobles.append(5 * 2)
# dobles.append(10 * 2)
# dobles.append(15 * 2)

# print("Lista de dobles:", dobles)


# Ejercicio 9: 
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla.

# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] # Lista original

# compras[2].append("jugo")
# compras[1][1] = "tallarines"
# compras[0].remove("pan")

# print(compras)


# Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#  Posición lista_anidada[0]: 15
#  Posición lista_anidada[1]: True
#  Posición lista_anidada[2][0]: 25.5
#  Posición lista_anidada[2][1]: 57.9
#  Posición lista_anidada[2][2]: 30.6
#  Posición lista_anidada[3]: False

# lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# print(lista_anidada)
