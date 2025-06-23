from fibonacci import fibonacci as fib

def main():
    posicion = int(input("Ingrese la posición de Fibonacci que desea calcular: "))
    print(f"El valor de Fibonacci en la posición {posicion} es: {fib(posicion)}")

if __name__ == "__main__":
    main()


# Otra forma de hacerlo
# for i in range(10):
#     print(fib(i))