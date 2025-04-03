# Práctico 3: Estructuras condicionales

# EJERCICIO 1:
#edad_mayor = 18
#edad_usuario = int(input("Ingresá tu edad: "))
#if edad_usuario >= edad_mayor:
    #print("Eres mayor de edad.")


# EJERCICIO 2:
#nota = int(input("Ingresá tu nota: "))

#if nota >= 6:
    #print("Aprobado")
#else:
    #print("Desaprobado")


# EJERCICIO 3:
#num = int(input("Ingresá un número par: "))

#if num % 2 == 0:
    #print("Ha ingresado un número par.")
#else: 
    #print("Por favor, ingrese un número par.")


# EJERCICIO 4:
#edad_usuario = int(input("Ingresá tu edad: "))

#if edad_usuario < 0:
    #print("Edad no válida.")
#elif edad_usuario < 12:
    #print("Eres un niño/a.")
#elif edad_usuario < 18:
    #print("Eres un/a adolescente.")
#elif edad_usuario < 30:
    #print("Eres un/a adulto/a joven.")
#else:
    #print("Eres un/a adulto/a.")


# EJERCICIO 5:
#contraseña = input("¡Hola! Ingrese aquí su contraseña: ")

#longitud_contraseña = len(contraseña)
#if 8 <= longitud_contraseña <= 14:
    #print("Ha ingresado una contraseña correcta.")
#else:
    #print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# EJERCICIO 6:
#import random
#from statistics import mean, median, mode

#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#def determinar_sesgo(num):
    #media = mean(num)
    #mediana = median(num)
    #try:
        #moda = mode(num)
    #except:
        #moda = "No única"
    
    #print(f"Media: {media}")
    #print(f"Mediana: {mediana}")
    #print(f"Moda: {moda}")
    
    #if media > mediana:
        #print("Sesgo positivo (derecha)")
    #elif media < mediana:
        #print("Sesgo negativo (izquierda)")
    #else:
        #print("No hay sesgo (simétrico)")

#determinar_sesgo(numeros_aleatorios)


# EJERCICIO 7:
#def modificar_string():
    #frase = input("¡Hola! Ingresá una frase o palabra: ")
    
    #if frase.endswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
        #frase += "!"
    
    #print(frase)

#modificar_string()


# EJERCICIO 8:
#def modificar_nombre():
    #nombre = input("¡Bienvenido/a! Ingresá tu nombre: ")
    #print("Seleccione una opción:")
    #print("1. Convertir a mayúsculas")
    #print("2. Convertir a minúsculas")
    #print("3. Convertir con la primera letra en mayúscula")
    
    #opcion = input("Ingrese 1, 2 o 3: ")
    
    #match opcion:
        #case "1":
            #nombre = nombre.upper()
        #case "2":
            #nombre = nombre.lower()
        #case "3":
            #nombre = nombre.title()
        #case _:
            #print("Opción no válida.")
            #return
    
    #print("Resultado:", nombre)

#modificar_nombre()


# EJERCICIO 9:
#def clasificar_terremoto():
    #try:
        #magnitud = float(input("Ingrese la magnitud del terremoto: "))
        
        #if magnitud < 3:
            #clasificacion = "Muy leve (imperceptible)"
        #elif magnitud < 4:
            #clasificacion = "Leve (ligeramente perceptible)"
        #elif magnitud < 5:
            #clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
        #elif magnitud < 6:
            #clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
        #elif magnitud < 7:
            #clasificacion = "Muy Fuerte (puede causar daños significativos)"
        #else:
            #clasificacion = "Extremo (puede causar graves daños a gran escala)"
        
        #print(f"Clasificación: {clasificacion}")
    #except ValueError:
        #print("Error: Ingrese un número válido.")

#clasificar_terremoto()


# EJERCICIO 10:
#def determinar_estacion():
    #hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()

    #if hemisferio not in ("N", "S"):
        #print("Hemisferio no válido.")
        #return
  
    #mes = int(input("¿Qué mes es? (1-12): "))
    #dia = int(input("¿Qué día es? (1-31): "))

    #if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        #print("Fecha no válida.")
        #return
    
    #estaciones = {
        #"N": [("Invierno", 12, 21, 3, 20), ("Primavera", 3, 21, 6, 20), ("Verano", 6, 21, 9, 20), ("Otoño", 9, 21, 12, 20)],
        #"S": [("Verano", 12, 21, 3, 20), ("Otoño", 3, 21, 6, 20), ("Invierno", 6, 21, 9, 20), ("Primavera", 9, 21, 12, 20)]
    #}
    
    #for estacion, mes_inicio, dia_inicio, mes_fin, dia_fin in estaciones[hemisferio]:
        #if (mes_inicio <= mes <= mes_fin) or (mes_inicio > mes_fin and (mes >= mes_inicio or mes <= mes_fin)):
            #if not ((mes == mes_inicio and dia < dia_inicio) or (mes == mes_fin and dia > dia_fin)):
                #print(f"Actualmente es {estacion}.")
                #return

#determinar_estacion()



    

