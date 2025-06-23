from suma_n_valores import suma_n_valores as suma_n

def main():
    # Lógica principal del programa
    num = int(input("Ingrese un número: "))
    # Llama a funciones o módulos necesarios
    print(f"La suma de los primeros {num} valores positivos es: {suma_n(num)}")

# para ejecutar el programa solo si el archivo se ejecuta directamente.
if __name__ == "__main__":
    main()