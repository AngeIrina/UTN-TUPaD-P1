from suma_n_primos import suma_n_primos as suma_n_primos_recursivo

def main():
    num = int(input("Ingrese un número entero positivo: "))
    if num <= 0:
        print("El número debe ser mayor que cero.")
        return
    suma = suma_n_primos_recursivo(num)
    print(f"La suma de los primeros {num} números primos es: {suma}")

if __name__ == "__main__":
    main()