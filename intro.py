import pygame
import sys

# incializando libreria
pygame.init()

# definiendo colores para dibujar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# creamos ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# crear bucle principal (todos los juegos corren en bucles principales)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # si le damos a la X, sale del juego
            sys.exit()

    # color que le ponemos a la pantalla
    screen.fill(WHITE)
    # dibujo de pantalla

    pygame.draw.line(screen, GREEN, [0, 100], [200, 300], 5)
    # dibujando un rectangulo
    pygame.draw.rect(screen, BLACK, (100, 100, 80, 80))
    # dibujando un circulo
    pygame.draw.circle(screen, BLACK, (200, 200), 30)
    # actualizar la pantalla con los cambios
    pygame.display.flip()
