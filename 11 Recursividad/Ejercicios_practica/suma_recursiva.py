"""Pasando una lista de numeros, obtener la suma de los mismos"""

def suma_lista(lista):
    if len(lista) == 0: # Caso base: si la lista está vacía, la suma es 0
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

lista = [1, 2, 3, 4, 5]
print(suma_lista(lista))  # Salida: 15

