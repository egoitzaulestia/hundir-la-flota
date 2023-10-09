# Importación de librerrías, variables y clases
import numpy as np
import time
from variables import DIMENSIONES_TABLERO
from classes import Tablero


# Función que imprime un tablero en formato visual con números de fila y columna,
# así como bordes y celdas que representan los valores del tablero.
def imprimir_tablero(tablero):
    DIMENSIONES_TABLERO = len(tablero)
    
    # Dibuja la parte superior del tablero con los números de columna
    print("    " + "   ".join(map(str, range(DIMENSIONES_TABLERO))))

    # Dibuja la línea separadora superior del tablero
    print("  " + "-" * (4 * DIMENSIONES_TABLERO))

    for i, fila in enumerate(tablero):
        # Dibuja el número de fila y los bordes laterales
        print(f"{i} |", end=" ")

        for valor in fila:
            # Reemplaza los valores 0 con espacios en blanco para una mejor visualización
            valor = " " if valor == 0 else valor

            # Dibuja cada celda y un separador
            print(f"{valor}", end=" | ")

        # Nueva línea para la siguiente fila y la línea separadora inferior
        print("\n  " + "-" * (4 * DIMENSIONES_TABLERO))


def main():
    # Bienvenida al juego
    print()
    print("Loading")  # Mensaje de carga simulada :)
    time.sleep(2)
    print("Loading .")
    time.sleep(.2)
    print("Loading . .")
    time.sleep(.1)
    print("Loading . . .")
    print()

    # Solicitar el nombre del/a jugador@
    player = input("Introduzca su nombre: ")
    print()

    # Mensaje de bienvenida personalizado
    print(f"¡Bienvenido a Hundir la Flota {player}!")  
    print()
    time.sleep(.5)

    # Espera a que el jugador presione Enter para iniciar el juego
    input("Presiona Enter para comenzar...")

    # Inicialización de tableros
    tablero_jugador = Tablero()
    tablero_maquina = Tablero()

    print("\nColocando barcos...")
    tablero_jugador.colocar_barcos_aleatoriamente()  # Colocación aleatoria de barcos en el tablero del jugador
    tablero_maquina.colocar_barcos_aleatoriamente()  # Colocación aleatoria de barcos en el tablero de la máquina

    while True:
        print("\nTablero del Jugador:")
        imprimir_tablero(tablero_jugador.tablero_disparos)  # Imprimir el tablero de disparos del jugador

        x = int(input("\nIntroduzca la coordenada de disparo X: "))  # Solicitar coordenada X para el disparo
        y = int(input("Introduzca la coordenada de disparo Y: "))  # Solicitar coordenada Y para el disparo

        resultado = tablero_maquina.disparar(x, y)  # Realizar disparo en el tablero de la máquina
        print(resultado)  # Imprimir el resultado del disparo

        if resultado.startswith("¡Impacto en"):
            if tablero_maquina.verificar_victoria():
                print("\n¡Has ganado!")  # Mensaje de victoria si se hunden todos los barcos de la máquina
                break

        print("\nTablero de la Máquina:")
        imprimir_tablero(tablero_maquina.tablero_disparos)  # Imprimir el tablero de disparos de la máquina
        print("\nTurno de la Máquina:")
        x = np.random.randint(0, DIMENSIONES_TABLERO - 1)  # Generar coordenada X aleatoria para el disparo de la máquina
        y = np.random.randint(0, DIMENSIONES_TABLERO - 1)  # Generar coordenada Y aleatoria para el disparo de la máquina

        resultado = tablero_jugador.disparar(x, y)  # Realizar disparo de la máquina en el tablero del jugador
        print(f"La Máquina dispara a ({x}, {y}): {resultado}")  # Imprimir el resultado del disparo de la máquina

        if resultado.startswith("¡Impacto en"):
            if tablero_jugador.verificar_victoria():
                print("\n¡La Máquina ha ganado!")  # Mensaje de victoria de la máquina si se hunden todos los barcos del jugador
                break
