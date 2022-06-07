import pygame


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 40
        self.h = 40

        self.rect = (self.x, self.y, self.w, self.h)
        self.image = None

    def draw(self, screen):
        self.image = pygame.draw.rect(screen, (82, 82, 82), self.rect)
        self.rect = (self.x, self.y, self.w, self.h)
