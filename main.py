import pygame
import levels
from level import Level
from network import Network

pygame.init()

bulletList = []

# run every frame
def drawWindow(screen, clock, player, player2, level, otherplayers):
    screen.fill((235, 235, 235))
    player.draw(screen, clock, level.tiles, otherplayers)
    player.move(clock)
    player2.draw(screen, clock, level.tiles, otherplayers)

    level.draw(screen, player, bulletList)
    # for tile in level.tiles:

    player.move(clock)
    pygame.display.update()


# contains main loop
def main():
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()

    n = Network()
    p = n.getP()

    level = Level(levels.testMap)

    running = True
    while running:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                p.shoot(bulletList)

        p2 = n.send(p)
        otherplayers = [p, p2]


        drawWindow(screen, clock, p, p2, level, otherplayers)
    pygame.quit()
    quit()


main()
