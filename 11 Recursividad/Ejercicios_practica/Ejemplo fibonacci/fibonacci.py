"""Calcula el valor de Fibonacci"""

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        """calcula el valor anterior y el anterior a ese en la secuencia de Fibonacci, y luego suma ambos resultados."""
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

if __name__ == "__main__":
    # Pruebas
    print(fibonacci(0)) # 0
    print(fibonacci(1)) # 1
    print(fibonacci(2)) # 1
    print(fibonacci(3)) # 2
    print(fibonacci(4)) # 3
    print(fibonacci(5)) # 5
    print(fibonacci(6)) # 8