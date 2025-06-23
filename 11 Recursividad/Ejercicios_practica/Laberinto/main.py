from laberinto_recur import resolver_laberinto as resolver


lab = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0]
    ]

camino = []
resolver(lab, 0, 0, camino)
print("Camino encontrado:", camino)