def resolver_laberinto(laberinto, x, y, camino):
    # Caso base: si estamos fuera de los limites o en un espacio bloqueado, detener.
    if x < 0 or y < 0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto[x][y] == 1:
        return False
    
    # Agregar la posicion actual al camino
    camino.append((x, y))

    # Caso base: si hemos llegado a la esquina inferior derecha, hemos encontrado el camino
    if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
        return True
    
    # Marcar la celda como visitada  para evitar ciclos
    laberinto[x][y] = 1

    # Intentar movernos en las cuatro direcciones
    if (resolver_laberinto(laberinto, x + 1, y, camino) or  # Abajo
        resolver_laberinto(laberinto, x, y + 1, camino) or  # Derecha
        resolver_laberinto(laberinto, x - 1, y, camino) or  # Arriba
        resolver_laberinto(laberinto, x, y - 1, camino)):   # Izquierda
        return True

    # Si ninguna dirección funciona, eliminar la posición actual del camino y desmarcar la celda.
    camino.pop()
    return False