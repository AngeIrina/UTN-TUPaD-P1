from repetir_frase import repetir_frase_recur as repetir

def main():
    frase = input("Escribe una frase: ")
    num = int(input("Cuantas veces quieres repetir la frase? "))

    repetir(num, frase) # Cambia el 5 por num para que sea dinamicocls

if __name__ == "__main__":
    main()