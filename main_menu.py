import pygame
import sys
from button import Button
from game import Game

pygame.init()

# Setting up resolution 
HEIGHT = 700
WIDTH = 1350
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BG = pygame.transform.scale(pygame.image.load("game_assets/menu_bg.jpeg"),
                            (WIDTH, HEIGHT))

# Initializing colours
WHITE = (255, 255, 255)
BROWN = (230, 217, 200)


def get_font(size):  # Returns Press-Start-2P in the desired size
  '''
	grabs font assets

  Parameters
  ----------
  size : int
  size of the text font being used

  Returns
  ------------------
  tuple
  font asset and size
  '''
  return pygame.font.Font("game_assets/Candelabra.ttf", size)


def main_menu(user_difficulty='Amateur'):
  '''
  by default the user diffuculty is Amateur

  Parameters
  ----------
  user_difficulty = str
  	Amateur


  Returns
  ------------------
  nothing
  '''
  while True:
    WINDOW.blit(BG, (0, 0))

    MENU_TEXT = get_font(100).render("Medieval Castle Defenders", True, WHITE)
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    DIFFICULTY_LEVEL_TEXT = get_font(30).render(
      f"Difficulty: {user_difficulty}", True, WHITE)
    DIFFICULTY_LEVEL_RECT = DIFFICULTY_LEVEL_TEXT.get_rect(center=(640, 660))

    MENU_BUTTON = pygame.transform.scale(
      pygame.image.load("game_assets/Medeival_Button.png"), (400, 140))

    PLAY_BUTTON = Button(image=MENU_BUTTON,
                         pos=(640, 250),
                         text_input="PLAY",
                         font=get_font(50),
                         base_color=WHITE,
                         hovering_color=BROWN)
    DIFFICULTY_BUTTON = Button(image=MENU_BUTTON,
                               pos=(640, 400),
                               text_input="DIFFICULTY",
                               font=get_font(50),
                               base_color=WHITE,
                               hovering_color=BROWN)
    QUIT_BUTTON = Button(image=MENU_BUTTON,
                         pos=(640, 550),
                         text_input="QUIT",
                         font=get_font(50),
                         base_color=WHITE,
                         hovering_color=BROWN)

    WINDOW.blit(MENU_TEXT, MENU_RECT)
    WINDOW.blit(DIFFICULTY_LEVEL_TEXT, DIFFICULTY_LEVEL_RECT)

    MENU_MOUSE_POS = pygame.mouse.get_pos()

		#makes the play button
    for button in [PLAY_BUTTON, DIFFICULTY_BUTTON, QUIT_BUTTON]:
      button.changeColor(MENU_MOUSE_POS)
      pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
      button.update(WINDOW)

		#establishes what to do if a button is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
          return 'Play'
        if DIFFICULTY_BUTTON.checkForInput(MENU_MOUSE_POS):
          return 'Difficulty'
        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
          pygame.quit()
          sys.exit()

    pygame.display.update()

def play(difficulty):
    '''
		runs the main menu
		
		Parameters
		----------
		nothing 
		
		Returns
		------------------
		nothing
    '''

    waves = [[1, 0, 1],
    [50, 0, 0],
    [100, 0, 0],
    [0, 20, 0],
    [0, 50, 0 ],
    [0, 100, 0],
    [20, 100, 0],
    [50, 100, 0],
    [100, 100, 0],
    [0, 0, 50, 3],
    [20, 0, 100],
    [20, 0, 150],
    [200, 100, 200]]

    if difficulty == 'Experienced':
      waves = [[2, 0, 2],
    [100, 0, 0],
    [200, 0, 0],
    [0, 40, 0],
    [0, 100, 0 ],
    [0, 200, 0],
    [40, 200, 0],
    [100, 200, 0],
    [200, 200, 0],
    [50, 0, 6],
    [40, 0, 200],
    [40, 0, 300],
    [400, 200, 400]]
    
    elif difficulty == 'Expert':
      waves = [[3, 0, 0],
    [150, 0, 0],
    [300, 0, 0],
    [0, 60, 0],
    [0, 150, 0 ],
    [0, 300, 0],
    [60, 300, 0],
    [150, 300, 0],
    [300, 300, 0],
    [10, 50, 3],
    [20, 0, 100],
    [20, 22, 150],
    [500, 300, 1000]]
  
    game = Game(WINDOW, waves)
    game.run()


def difficulty():
  '''
  allows the user to pick the difuculty  

  Parameters
  ----------
  nothing 

  Returns
  ------------------
  str
  Retdifficultyurns the difficulty either Amateur/Experienced/Expert
  '''
  while True:
    WINDOW.blit(BG, (0, 0))

    DIFFICULTY_TEXT = get_font(100).render("Difficulty", True, WHITE)
    DIFFICULTY_RECT = DIFFICULTY_TEXT.get_rect(center=(640, 100))

    DIFFICULTY_BUTTON = pygame.transform.scale(
      pygame.image.load("game_assets/Medeival_Button.png"), (400, 150))

    AMATEUR_BUTTON = Button(image=DIFFICULTY_BUTTON,
                            pos=(640, 250),
                            text_input="AMATEUR",
                            font=get_font(50),
                            base_color=WHITE,
                            hovering_color=BROWN)
    EXPERIENCED_BUTTON = Button(image=DIFFICULTY_BUTTON,
                                pos=(640, 400),
                                text_input="EXPERIENCED",
                                font=get_font(50),
                                base_color=WHITE,
                                hovering_color=BROWN)
    EXPERT_BUTTON = Button(image=DIFFICULTY_BUTTON,
                           pos=(640, 550),
                           text_input="EXPERT",
                           font=get_font(50),
                           base_color=WHITE,
                           hovering_color=BROWN)

    WINDOW.blit(DIFFICULTY_TEXT, DIFFICULTY_RECT)

    DIFFICULTY_MOUSE_POS = pygame.mouse.get_pos()

    for button in [AMATEUR_BUTTON, EXPERIENCED_BUTTON, EXPERT_BUTTON]:
      button.changeColor(DIFFICULTY_MOUSE_POS)
      pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
      button.update(WINDOW)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if AMATEUR_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
          return 'Amateur'
        if EXPERIENCED_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
          return 'Experienced'
        if EXPERT_BUTTON.checkForInput(DIFFICULTY_MOUSE_POS):
          return 'Expert'

    pygame.display.update()


def run():
  '''
  runs the main menu

  Parameters
  ----------
  nothing 

  Returns
  ------------------
  nothing
  '''
  game_page = 'Main'
  user_difficulty = 'Amateur'
  while True:
    if game_page == 'Main':
      game_page = main_menu(user_difficulty)
    elif game_page == 'Play':
      play(user_difficulty)
    elif game_page == 'Difficulty':
      user_difficulty = difficulty()
      game_page = 'Main'
