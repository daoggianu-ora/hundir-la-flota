# AI_LOG · Team Challenge Hundir la flota

Este registro no cuenta para la nota. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una parte, dejad el nivel en 0: también es un dato útil.

**Grupo:** Daniela 

**Herramientas usadas:**Gemini
> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por módulo

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA

| Módulo | Quién lo ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿Lo podríais repetir sin IA? (sí / en parte / no) |
|`variables.py`| Daniela| 2 | 2 | si |
|`clases.py` | Daniela | 2/3| 7 | algunas si, otras no, me cuesta recordar los pasos a seguir a pesar de entender la logica |
| `funciones.py` |Daniela  |2/3 | 3 | quizas en parte |
| `main.py` | | | | |
| `README.md` | | | | |

## Registro de prompts

Copiad este bloque por cada prompt que haya influido en vuestro código.

### Módulo X · Prompt 1

- **Objetivo:** qué queríais resolver.
- **Prompt:** copiadlo tal cual.
- **Respuesta relevante:** la parte que usasteis, resumida.
- **Cambios:** qué modificasteis y por qué.
- **Comprobación:** cómo verificasteis que funcionaba.
- **Decisión propia:** qué decidisteis vosotros.

### variables.py · Prompt 1

- **Objetivo:** estructurar la base del juego.
- **Prompt:** Tengo que estructurar la base del juego. Sin pasarme la solucion, ayudame a crearla paso paso.
- **Respuesta relevante:** piensa en qué elementos fijos necesitas. ¿Cómo definirías tú en Python la constante para guardar el tamaño del tablero (por ejemplo, usando una variable en mayúsculas)? ¡Intenta escribir esa primera línea!
- **Cambios:** -
- **Comprobación:** ninguna. 
- **Decisión propia:** escribir elenco de las variables con los datos fijos proporcionado por la guia.

### variables.py · Prompt 2 

- **Objetivo:** lectura fluyda de la estructura.
- **Prompt:** como se ve una base bien estructurada?
- **Respuesta relevante:** idea de su aspecto "anatómico":

# ==========================================
# 1. CONFIGURACIÓN DEL TABLERO
# ==========================================
# Aquí defines el tamaño de la cuadrícula
# NOMBRE_DE_VARIABLE = valor

- **Cambios:**  modificado las variables con los datos reales
- **Comprobación:** -
- **Decisión propia:** ninguna

### clases.py · Prompt 1

- **Objetivo:** entender como estructurar el modulo paso a paso.
- **Prompt:** estructura del modulo clases
- **Respuesta relevante:** 
    Importaciones + class Tablero + __init__
    mostrar() (para ver el tablero desde el principio)
    recibir_disparo(fila, columna)
    Limpiar pruebas (print() de depuración).
- **Cambios:** -
- **Comprobación:** run/terminal
- **Decisión propia:** -

### clases.py · Prompt 2

- **Objetivo:** entender cada paso.
- **Prompt:** repasamos el __init__ : para que sirve? y como se estructura (no utilices mis datos!)
- **Respuesta relevante:** 
    1.Encabezado del método: def __init__(self, ...):
    2.Asignación de atributos con self.: Dentro del cuerpo se guardan los valores iniciales en atributos propios del objeto (self.atributo = valor)
- **Cambios:** rescribir con los datos reales del juego
- **Comprobación:** run/terminal
- **Decisión propia:** -

### clases.py · Prompt 3

- **Objetivo:** aprender codigo np.ndarray
- **Prompt:** ¿como codifico esto:
tablero (np.ndarray): "Barcos del jugador y disparos recibidos.
disparos (np.ndarray): Solo los disparos recibidos, sin barcos." ?
- **Respuesta relevante:** 
    self.tablero = np.full((self.tamano, self.tamano), AGUA, dtype="<U2")
    self.disparos = np.full((self.tamano, self.tamano), AGUA, dtype="<U2")
- **Cambios:** -
- **Comprobación:** run/terminal
- **Decisión propia:** -

### clases.py · Prompt 4

- **Objetivo:** aprender codigo
- **Prompt:** mostrar() explicame el codigo
- **Respuesta relevante:** me ha mostrado y explicado cada linea
- **Cambios:** -
- **Comprobación:** run/terminal
- **Decisión propia:** -

### clases.py · Prompt 5

- **Objetivo:** aprender codigo
- **Prompt:** en recibir disparos que metodo utilizamos? dame pistas!
- **Respuesta relevante:** usar estructuras básicas que ya conoces: leer una posición de tu array de NumPy y tomar decisiones con if / elif / else
- **Cambios:** -
- **Comprobación:** run/terminal
- **Decisión propia:** -

### clases.py · Prompt 6

- **Objetivo:** aprender codigo
- **Prompt:** ¿ que metodo en colocar_barcos() ? base docstring y ejemplo code
- **Respuesta relevante:** el método que estás creando es def colocar_barcos(self) -> None: dentro de class Tablero, y por dentro combina bucles (for y while), random y comprobaciones sobre self.tablero (usando self.tamano, self.barcos, AGUA y BARCO importados de variables.py).
- **Cambios:** -
- **Comprobación:** run/terminal
- **Decisión propia:** -

### clases.py · Prompt 7

- **Objetivo:** aprender codigo
- **Prompt:** no se hacer un bucle tan largo y menos la comprobacion del bucle. explicame todo  por favor
- **Respuesta relevante:** La clave para no perderte es partirlo en piezas cortas (o incluso en pequeños pasos mentales) y entender qué revisa la comprobación.
- **Cambios:** -
- **Comprobación:** run/terminal
- **Decisión propia:** -

### funciones.py · Prompt 1

- **Objetivo:** imprimir instrucciones 
- **Prompt:** pista sobre imprimir instrucciones
- **Respuesta relevante:** Saludo y objetivo: imprimir MENSAJE_BIENVENIDA y explicar que hay que hundir todos los barcos del rival. Coordenadas: indicar que en cada turno se eligen fila y columna entre 0 y TABLERO - 1. Símbolos: mostrar qué representa cada constante (AGUA, BARCO, TOCADO, FALLO).
- **Cambios:** -
- **Comprobación:** -
- **Decisión propia:** -

### funciones.py · Prompt 2

- **Objetivo:** codigo correcto.
- **Prompt:** pista para la funcion pedir y validar las coordenadas del jugador
- **Respuesta relevante:** while True: / try ... except ValueError: / 0 <= fila <= limite_maximo / return fila, columna 
- **Cambios:** agregar datos
- **Comprobación:** terminal
- **Decisión propia:** -

### funciones.py · Prompt 3

- **Objetivo:** disparar al azar.
- **Prompt:** Por favor, ayudame a crear la función para que la máquina dispare a una casilla al azar del tablero sin que repita casillas donde ya disparó antes
- **Respuesta relevante:** el codigo
- **Cambios:** - 
- **Comprobación:** terminal
- **Decisión propia:** copiarlo tal y cual