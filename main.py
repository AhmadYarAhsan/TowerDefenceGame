import pygame

# Setting up display resolution and initally running program
if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((1350, 700))
    from main_menu import run
    mainMenu = run()
