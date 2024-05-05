import math
import pygame


class Tile:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def move_down(self):
        self.row += 1


class GameBoard:
    def __init__(self):
        self.num_of_tiles = 100
        self.tile_size = math.floor(800 / self.num_of_tiles)
        self.board_height = self.num_of_tiles * self.tile_size
        self.board_width = self.board_height
        self.tiles = [[Tile(row, col, self.tile_size) for col in range(
            self.num_of_tiles)] for row in range(self.num_of_tiles)]

        self.window = pygame.display.set_mode(
            (self.board_width, self.board_height))
        pygame.display.set_caption('falling sand')

        pygame.display.flip()

    def paint_tile(self, mouse_x, mouse_y):
        row = mouse_y // self.tile_size
        col = mouse_x // self.tile_size
        for i, j in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = i + row
            new_col = j + col
            self.tiles[new_row][new_col].activate()

    def draw_tiles(self):
        for row in range(self.num_of_tiles):
            for col in range(self.num_of_tiles):
                tile = self.tiles[row][col]
                if tile.active:
                    pygame.draw.rect(self.window, (255, 255, 255), (col *
                                     tile.size, row * tile.size, tile.size, tile.size))
                else:
                    pygame.draw.rect(self.window, (35, 35, 35), (col *
                                     tile.size, row * tile.size, tile.size, tile.size), 1)

    def reset(self):
        for row in range(self.num_of_tiles):
            for col in range(self.num_of_tiles):
                self.tiles[row][col].deactivate()

    def update_window(self):
        for row in range(self.num_of_tiles - 1, -1, -1):  # Iterate from bottom to top
            for col in range(self.num_of_tiles):
                tile = self.tiles[row][col]
                if tile.active:
                    if row < self.num_of_tiles - 1 and not self.tiles[row + 1][col].active:
                        self.tiles[row + 1][col], self.tiles[row][col] = self.tiles[row][col], self.tiles[row + 1][col]
                        tile.move_down()
                    elif row < self.num_of_tiles - 1 and col > 0 and col < self.num_of_tiles - 1 and not self.tiles[row + 1][col + 1].active:
                        self.tiles[row + 1][col +
                                            1], self.tiles[row][col] = self.tiles[row][col], self.tiles[row + 1][col + 1]
                    elif row < self.num_of_tiles - 1 and col > 0 and col < self.num_of_tiles - 1 and not self.tiles[row + 1][col - 1].active:
                        self.tiles[row + 1][col -
                                            1], self.tiles[row][col] = self.tiles[row][col], self.tiles[row + 1][col - 1]

    def draw_window(self):
        self.window.fill((0, 0, 0))
        self.draw_tiles()
        pygame.display.flip()
