import pygame
from gameBoard import GameBoard


def main():
    pygame.init()

    game_board = GameBoard()

    running = True
    drawing = False
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_board.reset()

            # draw
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

        if drawing:
            mouse_x, mouse_y = event.pos
            game_board.paint_tile(mouse_x, mouse_y)

        game_board.draw_window()
        game_board.update_window()

    pygame.quit()


if __name__ == "__main__":
    main()
