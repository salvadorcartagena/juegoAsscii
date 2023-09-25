import os
from typing import List, Tuple
from readchar import readkey, key  

def completar_paredes(cadena_laberinto, end):
    filas = cadena_laberinto.strip().split('\n')    
    while len(filas) < end + 1:
        filas.append("#" * (end + 1 - len(filas)))
    
    for i in range(len(filas)):
        while len(filas[i]) < end + 1:
            filas[i] += '#'

    laberinto_completo = '\n'.join(filas)
    return laberinto_completo

def cadena_a_matriz(cadena_laberinto):
    filas = cadena_laberinto.strip().split('\n')
    laberinto = [list(fila) for fila in filas]
    return laberinto

def mostrar_laberinto_limpiar(laberinto):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for fila in laberinto:
        print(''.join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial
    while (px, py) != posicion_final:
        mapa[py][px] = '☻'
        mostrar_laberinto_limpiar(mapa)
        teclado = readkey()
        nueva_px, nueva_py = px, py

        if teclado == key.UP and py > 0 and mapa[py - 1][px] != '#':
            nueva_py -= 1
        elif teclado == key.DOWN and py < len(mapa) - 1 and mapa[py + 1][px] != '#':
            nueva_py += 1
        elif teclado == key.LEFT and px > 0 and mapa[py][px - 1] != '#':
            nueva_px -= 1
        elif teclado == key.RIGHT and px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
            nueva_px += 1

        mapa[py][px] = ' '
        px, py = nueva_px, nueva_py

if __name__ == "__main__":
    
    laberinto_generado = """
..#############################
..#.......#.#.#...............#
#.#.#.#####.#.#.#####.#.#.#####
#...#...#.....#.#.....#.#.#...#
#####.#.#.###.#.#.#####.###.#.#
#.#...#.....#...#.#...#.....#.#
#.#.#########.#######.#####.###
#.#.#.....#.#.....#...#...#...#
#.#.###.###.#.#####.###.#.#.###
#.......#...........#...#.#...#
#.#.###.#.#######.###.#######.#
#.#.#.#.#.....#.....#.....#...#
###.#.###.#####.###.#.#########
#.......#.....#.#...#.........#
#.#.###.#.#.###.#####.#########
#.#.#...#.#...#.#.....#.......#
#.###.#########.#.###.#.#.#####
#...#.#.....#...#.#.#...#.....#
###.###.#.###.#####.#.#####.#.#
#.#.#...#...........#.#.#...#.#
#.#.#########.###.###.#.#######
#...#...#.......#.....#...#...#
#####.#####.###.#########.#.###
#.....#...#.#...#.#...#...#.#.#
#####.###.#####.#.#.#.#.#.#.#.#
#...#...#.....#.....#.#.#.....#
#.#.#.#.#.#####.###.###.#.###.#
#.#...#...........#.#.#.#.#...#
###.#.#.###.#.###.###.#.#####.#
#...#.#.#...#.#.............#..
##############################.

"""
    end = 30
    
    laberinto_completo = completar_paredes(laberinto_generado, end)
    
    mapa = cadena_a_matriz(laberinto_completo.strip())

    posicion_inicial = (0, 0)
    posicion_final = (end, end)

    main_loop(mapa, posicion_inicial, posicion_final)
