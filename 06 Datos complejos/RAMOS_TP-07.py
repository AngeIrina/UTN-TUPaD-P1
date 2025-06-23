# Práctico 7: Estructuras de Datos Complejas

# EJERCICIO 1
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print("Frutas y precios:")
# for fruta, precio in precios_frutas.items():
#     print(f"{fruta}: ${precio}")

# # EJERCICIO 2
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print("\nFrutas y precios actualizados:")
# for fruta, precio in precios_frutas.items():
#     print(f"{fruta}: ${precio}")

# # # EJERCICIO 3
# frutas = list(precios_frutas.keys())
# print("\nLista de frutas:")
# for fruta in frutas:
#     print(fruta)

# EJERCICIO 4
# class Persona:
#     def __init__(self, nombre, pais, edad):
#         self.nombre = nombre
#         self.pais = pais
#         self.edad = edad
      
#     def saludar(self):
#         print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# persona1 = Persona("Angela", "Argentina", 24)
# persona1.saludar()
# persona2 = Persona("Ana", "España", 25)
# persona2.saludar()

# EJERCICIO 5
# class Circulo:
#     def __init__(self, radio):
#         self.radio = radio

#     def calcular_area(self):
#         return 3.14 * (self.radio ** 2)

#     def calcular_perimetro(self):
#         return 2 * 3.14 * self.radio

# circulo1 = Circulo(5)
# print(f"Área del círculo: {circulo1.calcular_area()}")
# print(f"Perímetro del círculo: {circulo1.calcular_perimetro()}")

# EJERCICIO 6
# def estan_balanceados(cadena):
#     pila = []
#     pares = {')': '(', '}': '{', ']': '['}

#     for caracter in cadena:
#         if caracter in '({[':
#             pila.append(caracter) 
#         elif caracter in ')}]':
#             if not pila or pila[-1] != pares[caracter]:
#                 return False  
#             pila.pop()  

#     return len(pila) == 0  

# print(estan_balanceados("[(})]")) # False
# print(estan_balanceados("{[]}")) # True

# EJERCICIO 7
# from collections import deque
# class Banco:
#     def __init__(self):
#         self.cola = deque()

#     def agregar_cliente(self, cliente):
#         self.cola.append(cliente)
#         print(f"Cliente {cliente} agregado a la cola.")

#     def atender_cliente(self):
#         if self.cola:
#             cliente_atendido = self.cola.popleft()
#             print(f"Atendiendo al cliente: {cliente_atendido}")
#         else:
#             print("No hay clientes en la cola.")

#     def siguiente_cliente(self):
#         if self.cola:
#             print(f"Siguiente cliente en la fila: {self.cola[0]}")
#         else:
#             print("No hay clientes en la cola.")

# if __name__ == "__main__":
#     banco = Banco()
#     banco.agregar_cliente("Cliente 1") 
#     banco.agregar_cliente("Cliente 2") 
#     banco.siguiente_cliente() # muestra el primero en la cola
#     banco.atender_cliente() # atiende al primer cliente
#     banco.siguiente_cliente() # muestra el siguiente cliente en la cola
#     banco.atender_cliente() # atiende al segundo cliente
#     banco.atender_cliente()  # Intentar atender cuando no hay clientes

# EJERCICIO 8
# class Nodo:
#     def __init__(self, valor):
#         self.valor = valor
#         self.siguiente = None

# class ListaEnlazada:
#     def __init__(self):
#         self.cabeza = None

#     def insertar_al_inicio(self, valor):
#         nuevo_nodo = Nodo(valor)
#         nuevo_nodo.siguiente = self.cabeza
#         self.cabeza = nuevo_nodo

#     def mostrar(self):
#         actual = self.cabeza
#         while actual:
#             print(actual.valor)
#             actual = actual.siguiente

# EJERCICIO 9
#     def invertir(self):
#         anteriror = None
#         actual = self.cabeza
#         while actual:
#             siguiente = actual.siguiente
#             actual.siguiente = anteriror
#             anteriror = actual
#             actual = siguiente
#         self.cabeza = anteriror

# if __name__ == "__main__":
#     lista = ListaEnlazada()
#     lista.insertar_al_inicio(10)
#     lista.insertar_al_inicio(20)
#     lista.insertar_al_inicio(30)
#     print("Valores en la lista enlazada:")
#     lista.mostrar()
#     lista.invertir()
#     print("Lista enlazada invertida:")
#     lista.mostrar()


