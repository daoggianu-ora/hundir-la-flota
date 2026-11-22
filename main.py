import numpy as np
from clases import Tablero
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_maquina
from variables import (JUGADOR_1, JUGADOR_2, BARCO, MENSAJE_TURNO_JUGADOR, MENSAJE_TOCADO, MENSAJE_AGUA, MENSAJE_VICTORIA,MENSAJE_DERROTA)

mostrar_instrucciones() # muestra instrucciones y prepara tableros

tablero_jugador = Tablero(JUGADOR_1)
tablero_maquina = Tablero(JUGADOR_2)

tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()

casillas_disparadas_maquina = set() # guarda casillas disparadas por la maquina
 
while True:
    # mostrar tableros ocultando barcos enemigos
    tablero_jugador.mostrar(ocultar_barcos=False)
    tablero_maquina.mostrar(ocultar_barcos=True)

    # Turno jugador: dispara hasta tocar, evitando repetir coordenadas
    while True:
        print(f"\n{MENSAJE_TURNO_JUGADOR}")
        fila, columna = pedir_coordenadas()
        resultado = tablero_maquina.recibir_disparos(fila, columna)

        if resultado == "repetido":
            print("Ya has disparado a esa casilla. Elige otra.")
            continue

        if resultado == "tocado":
            print(MENSAJE_TOCADO)
            if np.sum(tablero_maquina.tablero == BARCO) == 0:
                print(f"\n{MENSAJE_VICTORIA} ¡Has hundido toda la flota de {JUGADOR_2}!")
                break
            tablero_maquina.mostrar(ocultar_barcos=True)
            continue

        print(MENSAJE_AGUA)
        break

    # check jugador si ha ganado o no despues de disparar
    if np.sum(tablero_maquina.tablero == BARCO) == 0:
        break

    # Turno maquina: dispara hasta tocar o agua
    while True:
        fila_ia, col_ia = disparo_maquina(casillas_disparadas_maquina)
        resultado_ia = tablero_jugador.recibir_disparos(fila_ia, col_ia)
        print(f"\n{JUGADOR_2} dispara a ({fila_ia}, {col_ia})...")

        if resultado_ia == "tocado":
            print(MENSAJE_TOCADO)
            if np.sum(tablero_jugador.tablero == BARCO) == 0:
                print(f"\n{MENSAJE_DERROTA}. {JUGADOR_2} ha hundido toda tu flota.")
                break
            continue

        print(MENSAJE_AGUA)
        break

    # check maquina si ha ganado o no despues de disparar
    if np.sum(tablero_jugador.tablero == BARCO) == 0:
        break