# ========================================================
# 1. DIMENSIONES TABLERO
# ========================================================
# Tamaño tablero 10x10 por jugador
TABLERO = 10

# ========================================================
# 2. JUGADORES
# ========================================================
# Numero de jugadores: 2
JUGADOR_1 = "Humano"
JUGADOR_2 = "Maquina"

# ========================================================
# 3. FLOTA
# ========================================================
# Tamaño de los barcos y cuantos hay de cada tipo
BARCOS = {
    "barco_muy_grande": {"casillas": 4, "cantidad": 1},
    "barco_grande": {"casillas": 3, "cantidad": 2},
    "barco_mediano": {"casillas": 2, "cantidad": 3},
    "barco_pequeno": {"casillas": 1, "cantidad": 4}

}

# ========================================================
# 4. SÍMBOLOS DENTRO DEL TABLERO
# ========================================================
# Caracteres representativos del estado de la casilla
AGUA = "~~"  # sin barco
BARCO = "B"  # con barco
TOCADO = "X" # disparo ok
FALLO = "."  # disparo al agua

# ========================================================
# 5. MENSAJES 
# ========================================================
MENSAJE_BIENVENIDA = "¡Bienvenido a este juego!"
MENSAJE_TURNO_JUGADOR = "Es tu turno. Dispara:"
MENSAJE_TOCADO = "¡Tocado!"
MENSAJE_AGUA = "¡Agua!"
MENSAJE_VICTORIA = "¡Enhorabuena!"
MENSAJE_DERROTA = "Has perdido"