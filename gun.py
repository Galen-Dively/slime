import pygame
import math
import pickle

class Gun:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.maxClip = 20
        self.image = pygame.transform.scale(pygame.image.load("gun.png"), (6, 29))
        self.rect = self.image.get_rect(center=(self.x, self.y - 3))
        self.angle = 0

    def draw(self, screen, x, y):
        self.x = x
        self.y = y
        self.rotate(screen)

    def rotate(self, screen):
        rotatedImage = pygame.transform.rotozoom(self.image, self.angle, 1)
        rotatedRect = rotatedImage.get_rect(center=(self.x, self.y + 3))
        screen.blit(rotatedImage, rotatedRect)
        self.aim(rotatedRect.x, rotatedRect.y)

    def aim(self, x, y):
        mousePos = pygame.mouse.get_pos()
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        relX = mouseX - self.x
        relY = mouseY - self.y
        self.angle = (180/math.pi) * -math.atan2(relY, relX) - 90

