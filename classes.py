# Importación de librerías y variables
import numpy as np
import random
from variables import DIMENSIONES_TABLERO, BARCOS

# Creamos una clase llamada 'Tablero' que representa el tablero de juego
class Tablero:

    # Cuando creamos un nuevo tablero, inicializamos dos matrices vacías que representan el tablero principaly el tablero de disparos.
    def __init__(self):
        # Creamos 2 tableros de 10x10 
        self.tablero = np.full((DIMENSIONES_TABLERO, DIMENSIONES_TABLERO), " ")  # El tablero principal
        self.tablero_disparos = np.full((DIMENSIONES_TABLERO, DIMENSIONES_TABLERO), "S")  # El tablero de disparos
    
    # Método que coloca barcos aleatoriamente en el tablero principal
    def colocar_barcos_aleatoriamente(self):
        for barco, size in BARCOS.items():
            while True:
                # Generamos posiciones aleatorias y orientación para el barco
                x = np.random.randint(0, DIMENSIONES_TABLERO - 1)
                y = np.random.randint(0, DIMENSIONES_TABLERO - 1)
                orientacion = random.choice(["horizontal", "vertical"])

                # Validamos si es posible colocar el barco en esa posición
                if self.validar_posicion(x, y, size, orientacion):
                    # Si es posible, colocamos el barco en el tablero
                    self.colocar_barco(x, y, size, orientacion, barco)
                    break

    # Método que verifica si es posible colocar un barco en una posición específica
    def validar_posicion(self, x, y, size, orientacion):
        # Verificamos si el barco cabe dentro del tablero horizontalmente
        if orientacion == "horizontal":
            if x + size > DIMENSIONES_TABLERO:  # Si la posición inicial + tamaño del barco supera las dimensiones del tablero
                return False  # No es posible colocar el barco en esta posición
            # Verificamos si no hay otros barcos en la posición deseada
            for i in range(size):
                if self.tablero[x + i][y] != " ":  # Si hay algo en la posición deseada
                    return False  # No es posible colocar el barco en esta posición
        elif orientacion == "vertical":
            if y + size > DIMENSIONES_TABLERO:  # Si la posición inicial + tamaño del barco supera las dimensiones del tablero
                return False  # No es posible colocar el barco en esta posición
            # Verificamos si no hay otros barcos en la posición deseada
            for i in range(size):
                if self.tablero[x][y + i] != " ":  # Si hay algo en la posición deseada
                    return False  # No es posible colocar el barco en esta posición
        return True  # Si no hay problemas de espacio ni otros barcos, es posible colocar el barco aquí

    # Método que coloca realmente el barco en el tablero
    def colocar_barco(self, x, y, size, orientacion, barco):
        if orientacion == "horizontal":
            # Colocamos el barco en el tablero horizontalmente
            for i in range(size):
                self.tablero[x + i][y] = barco
        elif orientacion == "vertical":
            # Colocamos el barco en el tablero verticalmente
            for i in range(size):
                self.tablero[x][y + i] = barco

    # Esta método representa un disparo en el tablero
    def disparar(self, x, y):
        if self.tablero[x][y] != " ":
            # Si hay un barco en la posición del disparo, lo marcamos como impactado y también en el tablero de disparos
            barco = self.tablero[x][y]
            self.tablero[x][y] = "X"  # Marcamos como impactado
            self.tablero_disparos[x][y] = "X"  # Marcamos como disparado
            return f"¡Impacto en {barco}!"
        else:
            # Si no hay un barco en la posición del disparo, lo marcamos como agua en el tablero de disparos
            self.tablero_disparos[x][y] = "-"  # Marcamos como disparado
            return "Agua"
    
    # Método que verifica si todos los barcos han sido impactados, es decir, si el jugador ha ganado
    def verificar_victoria(self):
        return np.all(self.tablero_disparos == "X")
