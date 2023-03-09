import pygame, sys

# incializando libreria
pygame.init()

# creamos ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# crear bucle principal (todos los juegos corren en bucles principales)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # si le damos a la X, sale del juego
            sys.exit()
