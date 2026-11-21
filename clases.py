import numpy as np
import random
from variables import TABLERO, BARCOS, AGUA, BARCO, TOCADO, FALLO

class Tablero:
    """
    Tablero de jugador humano.
    
    Attributes:
        id_jugador (str): Identifica el jugador humano.
        tamano (int): tamano x tamano.
        barcos(dict): Diccionario con tipo de barco, casilla y cantidad.
        tablero (np.ndarray): Barcos del jugador y disparos recibidos.
        disparos (np.ndarray): Sin barcos, disparos recibidos.
    """
    def __init__(self, id_jugador : str):
        self.id_jugador = id_jugador
        self.tamano = TABLERO
        self.barcos = BARCOS
        self.tablero = np.full((self.tamano, self.tamano), AGUA, dtype="<U2")
        self.disparos = np.full((self.tamano, self.tamano), AGUA, dtype="<U2")

    def mostrar(self, ocultar_barcos: bool = False) -> None:
        """
        Imprime el tablero en consola con índices de filas y columnas.

        Args:
            ocultar_barcos (bool, optional): Si es True, muestra solo disparos
                sin revelar los barcos. Por defecto False.
        """
        matriz = self.disparos if ocultar_barcos else self.tablero

        print(f"\n--- Tablero de {self.id_jugador} ---")
        encabezado_cols = "   " + " ".join(f"{col:>2}" for col in range(self.tamano))
        print(encabezado_cols)

        for fila in range(self.tamano):
            contenido_fila = " ".join(f"{celda:>2}" for celda in matriz[fila])
            print(f"{fila:>2} {contenido_fila}")

    def recibir_disparos(self, fila: int, columna:int):
        """
        Un disparo por casilla (fila, columna).
        
        Args:
            fila: (int): fila del disparo.
            columna (int): columna del disparo.
        Returns:
            str: "tocado", "agua" o "repetido".
        """

        casilla = self.tablero[fila, columna]

        if casilla in (TOCADO, FALLO):
              return "repetido"
        if casilla == BARCO:
              self.tablero[fila, columna] = TOCADO
              self.disparos[fila, columna] = TOCADO
              return "tocado"

        self.tablero[fila, columna] = FALLO
        self.disparos[fila, columna] = FALLO
        return "agua"

    def colocar_barcos(self) -> None:
        """
        Coloca aleatoriamente los barcos de la flota en el tablero.

        Comprobar que cada barco quede dentro de los límites del tablero y que
        no se superponga con otros barcos ya colocados.
        """
        for _, datos in self.barcos.items():
            eslora = datos["casillas"]
            cantidad = datos["cantidad"]

            for _ in range(cantidad):
                colocado = False

                while not colocado:
                    orientacion = random.choice(["H", "V"])
                    fila_inicio = random.randrange(self.tamano)
                    col_inicio = random.randrange(self.tamano)

                    if orientacion == "H":
                        coordenadas = [
                            (fila_inicio, col_inicio + i) for i in range(eslora)
                        ]
                    else:
                        coordenadas = [
                            (fila_inicio + i, col_inicio) for i in range(eslora)
                        ]

                    dentro_y_libre = True
                    for f, c in coordenadas:
                        if not (0 <= f < self.tamano and 0 <= c < self.tamano):
                            dentro_y_libre = False
                            break
                        if self.tablero[f, c] != AGUA:
                            dentro_y_libre = False
                            break

                    if dentro_y_libre:
                        for f, c in coordenadas:
                            self.tablero[f, c] = BARCO
                        colocado = True