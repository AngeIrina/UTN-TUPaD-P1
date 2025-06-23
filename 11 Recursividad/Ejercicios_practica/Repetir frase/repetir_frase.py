"""Una funcion que reciba una farse y un numero n, y repita la frase n veces"""

def repetir_frase_recur(num, frase):
    if num >= 1:
        print(frase)
        repetir_frase_recur(num - 1, frase)

# Esto es opcional, es como un test, prueba rapida de la funcion
if __name__ == "__main__": 
 print(repetir_frase_recur(5, "Hola Mundo")) 

# Otra forma de hacerlo
# def repetir_frase(num, frase):
#     if num == 0:
#         return
#     print(frase)
#     repetir_frase(num - 1, frase)