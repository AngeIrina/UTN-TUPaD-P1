"""Funcion que permite sumar n valores primos"""

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_n_primos(n):
   if n == 1:
        return 0
   elif es_primo(n):
        return n + suma_n_primos(n - 1)
   else:
        return suma_n_primos(n - 1)

if __name__ == "__main__":
    print(suma_n_primos(5))  # Suma de los primeros 5 números primos