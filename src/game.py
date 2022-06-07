import pygame
import src.levels as level
from src.level import Level
from src.network import Network

class Game:
    def __init__(self):
        self.screen  = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()

        self.bulletList = [] # a list of all bullets in the scene

        # get player stuff
        self.network = Network()
        self.player = self.network.getP()
        self.playerList = []
        # game states
        self.running = True


        self.level = Level(levels.testMap)
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(60) # sets max 60fps
            for event in pyame.event.get():
                self.running = False
            # checking for mouse press to shoot
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot(bulletList) # add the bullet


            self.tick()
            screen.fill((235, 235, 235))
            self.render()
            pygame.display.update()
        pygame.quit()
        quit()

    def render(self):
        for player in self.playerList:
            player.draw(self.screen, self.clock, self.level.tiles, self.playerList)
            player.move(self.clock)
        self.level.draw(self.screen, self.player, self.bulletList)


    def tick(self):
        self.playerList = [self.player, self.netowork.send(self.player)]
