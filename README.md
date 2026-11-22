# hundir-la-flota

Juego de **Hundir la Flota** por consola desarrollado en Python para el *Team Challenge* del Sprint 5, jugado entre un jugador humano y la máquina sobre un tablero de 10x10.

## Estructura del repositorio

- `variables.py`: constantes de configuración, símbolos del tablero, definición de la flota y mensajes del juego.
- `clases.py`: clase `Tablero` con colocación de barcos, gestión de disparos y visualización.
- `funciones.py`: funciones auxiliares para mostrar instrucciones, pedir y validar coordenadas y gestionar el disparo de la máquina.
- `main.py`: punto de entrada y bucle principal de la partida.
- `requirements.txt`: librerias externas necesarias para ejecutar el proyecto.
- `AI_LOG.md`: registro del uso de IA durante el desarrollo.

## Reglas y dinámica de juego

- **Tablero:** cuadrícula de `10x10` (filas y columnas numeradas del `0` al `9`).
- **Símbolos:**
  - `~~`: agua sin disparar.
  - `B`: barco propio.
  - `X`: disparo acertado (tocado).
  - `.`: disparo al agua (fallo).
- **Flota por jugador (20 casillas en total):**
  - 1 barco de 4 casillas.
  - 2 barcos de 3 casillas.
  - 3 barcos de 2 casillas.
  - 4 barcos de 1 casilla.
- **Turnos y victoria:** el jugador humano y la máquina se alternan disparando; acertar permite repetir disparo y no se pueden repetir casillas ya disparadas. Gana quien hunda primero toda la flota rival.

## Instalación y ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt