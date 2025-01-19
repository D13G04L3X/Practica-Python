import pygame       # Libreria para manejar gráficos, eventos, sonidos y lógica de los juegos
import sys          # Permitir cerrar el programa limpiamente
import random       # Generar valores aleatorios, para la posición de la comida

# Inicializar Pygame
pygame.init()       # Inicia todos los módulos de Pygame para poderlo usar en el juego

# Configurar la ventana
WIDTH, HEIGHT = 750, 450        # Definir el tamaño de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))       # Crear la ventana del juego
pygame.display.set_caption("Snake game")        # Definir el título de la ventana

# Colores. Cada color se define como una tupla de valores RGB
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

# Configuración del reloj. Controlar la velocidad del juego, limitando los cuadros por segundo
clock = pygame.time.Clock()

# Variables del Snake
snake_pos = [100,50]        # Definir la posición inicial de la cabeza de la serpiente
snake_body = [[100,50],[90,50],[80,50]]         # Lista de bloques que representan el cuerpo del snake
direction = 'RIGHT'     # Dirección actual del movimiento a la derecha

# Variables de la comida

# Puntuación