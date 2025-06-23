"""Realizar la suma de los primeros n valores positivos"""

def suma_n_valores(num):
    if num == 0:
        return 0
    else:
        return num + suma_n_valores(num - 1)
    
if __name__ == "__main__":
    print(suma_n_valores(3))