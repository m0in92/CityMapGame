import pygame
import sys
from elements import Map, Vehicle


# initialize screen
pygame.init()
cell_num = 5
cell_size = 40
screen = pygame.display.set_mode((cell_size*cell_num, cell_size*cell_num))
pygame.display.set_caption("Basic Street Map")
clock = pygame.time.Clock()

map = Map(cell_size, cell_num)
vehicle = Vehicle(cell_size)

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # vehicle.move()
    map.draw_element()
    vehicle.draw()
    vehicle.move()
    print(pygame.sprite.spritecollideany(map, vehicle))
    pygame.display.update()
    clock.tick(60) # Frame rate set to 60