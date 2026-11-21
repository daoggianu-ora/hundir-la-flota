import random
from clases import Tablero
import variables

def mostrar_instrucciones() -> None:
    """
    Muestra por consola las instrucciones básicas del juego Hundir la Flota.
    """
    print(variables.MENSAJE_BIENVENIDA)
    print("\n--- INSTRUCCIONES ---")
    print("El objetivo del juego es hundir toda la flota rival antes de que hundan la tuya.")
    print(
        f"El tablero tiene tamaño {variables.TABLERO}x{variables.TABLERO}, "
        f"así que las filas y columnas van de 0 a {variables.TABLERO - 1}."
    )
    print("\nSímbolos en el tablero:")
    print(f"  {variables.AGUA} : Agua sin disparar")
    print(f"  {variables.BARCO}  : Barco propio")
    print(f"  {variables.TOCADO}  : Disparo acertado (tocado)")
    print(f"  {variables.FALLO}  : Disparo al agua (fallo)")
    print("\nFlota por jugador:")
    for nombre_barco, datos in variables.BARCOS.items():
        print(f"  - {nombre_barco}: {datos['cantidad']} de {datos['casillas']} casillas")


def pedir_coordenadas() -> tuple[int, int]:
    """
    Pide al jugador una fila y una columna válidas dentro del tablero
    y las devuelve como una tupla (fila, columna).
    """
    limite_maximo = variables.TABLERO - 1

    while True:
        try:
            fila = int(input(f"Introduce la fila (0 a {limite_maximo}): "))
            columna = int(input(f"Introduce la columna (0 a {limite_maximo}): "))
        except ValueError:
            print("Entrada no válida. Escribe solo números enteros.")
            continue

        if 0 <= fila <= limite_maximo and 0 <= columna <= limite_maximo:
            return fila, columna

        print(f"Coordenadas fuera de rango. Deben estar entre 0 y {limite_maximo}.")


def disparo_maquina(casillas_disparadas: set[tuple[int, int]]) -> tuple[int, int]:
    """
    Elige aleatoriamente una casilla del tablero que la máquina aún no haya disparado,
    la registra en casillas_disparadas y devuelve (fila, columna).
    """
    limite_maximo = variables.TABLERO - 1

    while True:
        fila = random.randint(0, limite_maximo)
        columna = random.randint(0, limite_maximo)
        coordenada = (fila, columna)

        if coordenada not in casillas_disparadas:
            casillas_disparadas.add(coordenada)
            return fila, columna

