from src.obstacles import Block
from src.bullet import Bullet

class Level:
    def __init__(self, level):
        self.tiles = []

        rowCount = 0
        for row in level:
            colCount = 0
            for tile in row:
                if tile == 1:
                    tile = Block(colCount*40, rowCount*40)
                    self.tiles.append(tile)
                colCount += 1
            rowCount += 1

    def draw(self, screen, player, tile):
        for tile in self.tiles:
            tile.draw(screen)
            player.updateCollisions(tile)
