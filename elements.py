import pygame.sprite
from pygame.math import Vector2


class Map(pygame.sprite.Sprite):
    def __init__(self, cell_size, cell_num):
        pygame.sprite.Sprite.__init__(self)
        self.cell_size = cell_size
        self.cell_num = cell_num
        self.non_roads = [Vector2(i,j) for i in [0,4] for j in range(self.cell_size-1)] + \
                     [Vector2(i, j) for j in [0, 4] for i in range(self.cell_size-1)] + \
            [Vector2(2,2)]
        self.screen = pygame.display.get_surface()

    @property
    def roads(self):
        roads_ = []
        for i in range(self.cell_num - 1):
            for j in range(self.cell_num - 1):
                if Vector2(i,j) not in self.non_roads:
                    roads_.append(Vector2(i,j))
        return roads_

    def draw_element(self):
        for block in self.non_roads:
            x_pos = int(self.cell_size * block.x)
            y_pos = int(self.cell_size * block.y)
            element_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, pygame.Color("green"), element_rect)

        for block in self.roads:
            x_pos = int(self.cell_size * block.x)
            y_pos = int(self.cell_size * block.y)
            element_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, (142, 146, 145), element_rect)


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, cell_size):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.cell_size = cell_size
        self.pos = Vector2(1,1)
        self.direction = Vector2(1,0)

    def draw(self):
        x_pos = self.cell_size * self.pos.x
        y_pos = self.cell_size * self.pos.y
        vehicle_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, pygame.Color("red"), vehicle_rect)

    def move(self):
        self.pos.x = self.pos.x + self.direction.x * 0.001
        print(self.rect.colliderect())

