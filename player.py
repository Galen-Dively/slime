import pygame
import random
from gun import Gun
from bullet import Bullet


class Player:
    def __init__(self, id):
        self.id = id
        self.x = random.randrange(100, 875)
        self.y = random.randrange(100, 875)
        self.w = 35
        self.h = 35
        self.speed = 5

        # self.gun = Gun(self.x, self.y)
        self.bulletCount = 0
        self.bulletList = []

        self.hp = 100

        self.lives = 5

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = 0
        self.color = (random.randrange(80, 200), (random.randrange(80, 200)), random.randrange(80, 200))

        # handling pushback from collision
        self.direction = 'up'


    def move(self, clock):
        pressed_keys = pygame.key.get_pressed()

        dt = clock.get_fps() / 1000 # delta time

        if pressed_keys[pygame.K_w]:
            self.y -= self.speed*dt
            self.direction = 'up'
        if pressed_keys[pygame.K_s]:
            self.y += self.speed*dt
            self.direction = 'down'
        if pressed_keys[pygame.K_a]:
            self.x -= self.speed*dt
            self.direction = 'left'
        if pressed_keys[pygame.K_d]:
            self.direction = 'right'
            self.x += self.speed*dt


    def draw(self, screen, clock, tiles, players):
        # object displayed
        self.image = pygame.draw.circle(screen, self.color, (self.rect[0], self.rect[1]), self.rect[2]//2)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h) # hidden for collisions
        # self.gun.draw(screen, self.x, self.y)
        for bullet in self.bulletList:
            bullet.draw(screen, clock, self.bulletList, tiles, players)




    def updateCollisions(self, obstacle):
        if self.rect.colliderect(obstacle.image):
            if self.x < obstacle.image.x:
                self.x = self.image.x + self.image.w / 2 - 2
            if self.x > obstacle.image.x:
                self.x = self.image.x + self.image.w / 2 + 2
            if self.image.y < obstacle.image.y:
                self.y = self.image.y + self.image.h / 2 - 2
            if self.image.y > obstacle.image.y:
                self.y = self.image.y + self.image.h / 2 + 2


    def shoot(self, bulletList):
        tarX = pygame.mouse.get_pos()[0]
        tarY = pygame.mouse.get_pos()[1]
        self.bulletList.append(Bullet(self.x, self.y, tarX, tarY, self.id))
        print(self.id)
        self.bulletCount += 1
        return bulletList

    def die(self):
        self.x = random.randrange(100, 875)
        self.y = random.randrange(100, 875)
