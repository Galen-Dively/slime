import pygame
import math

class Bullet:
    def __init__(self, x, y, destX, destY, player):
        self.id = player
        self.damage = 12
        self.x = x
        self.y = y
        self.destX = destX
        self.destY = destY
        self.time = 0
        self.rect = None
        self.shooting = True
        self.destRect = pygame.Rect(destX, destY, 10, 10)
        self.angle = 0
        self.playerHP = 0

        self.dx = self.destRect.x - self.x
        self.dy = self.destRect.y - self.y
        dist = math.hypot(self.dx, self.dy)
        self.dx = self.dx / dist
        self.dy = self.dy / dist

    def draw(self, screen, clock, bulletList, tile, players):
        self.x += self.dx*30*clock.get_fps() / 1000
        self.y += self.dy*30*clock.get_fps() / 1000
        self.rect = pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)


        for t in tile:
            if self.rect.colliderect(t.rect):
                try:
                    bulletList.pop(bulletList.index(self.rect))
                except Exception as e:
                    pass

        for player in players:
            if player.rect.colliderect(self.rect) and self.id != player.id:
                player.die()