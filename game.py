import pygame
import os
from enemies.goblin import Goblin
from enemies.ogre import Ogre
from enemies.orc import Orc
from towers.magicTower import UpgradedMagicTower, SimpleMagicTower
from menu import VerticalMenu, PlayPauseButton
import time
import random
pygame.font.init()
pygame.init()

# path for enemies to follow
path =  [(549, 680), (442, 617), (274, 586), (163, 573), (116, 465), (124, 326), (163, 187), (257, 135), (372, 118), (508, 109), (655, 124), (787, 110), (907, 113), (999, 131), (1104, 158), (1198, 212), (1203, 275), (1134, 328), (1008, 364), (839, 344), (668, 363), (644, 459), (703, 560), (846, 576)]

# importing the assets for classes
lives_image = pygame.image.load(os.path.join("game_assets","heart.png")).convert_alpha()
coin_image = pygame.image.load(os.path.join("game_assets","coin.png")).convert_alpha()
side_image = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","side.png")).convert_alpha(), (120, 500))

magicTower1 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","simple_buy_tower.png")).convert_alpha(), (75, 75))
magicTower2 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","upgraded_buy_tower.png")).convert_alpha(), (75, 75))

play_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","button_start.png")).convert_alpha(), (75, 75))
pause_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","button_pause.png")).convert_alpha(), (75, 75))

sound_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","button_sound.png")).convert_alpha(), (75, 75))
sound_button_off = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","button_sound_off.png")).convert_alpha(), (75, 75))

wave_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","wave.png")).convert_alpha(), (225, 75))

# Names the different tower types

attack_tower_names = ["magicTower1", "magicTower2"]
support_tower_names = ["range", "damage"]

# load music
pygame.mixer.music.load(os.path.join("game_assets", "music.mp3"))

class Game:
    '''
		Main class where everything game related starts/happens
		
    Attributes
    ----------
    width : int
	    The width of the main menu 
	 	length : int
	 		The length of the main menu
		win : str
			used to draw picture
	 	enemys : list(int)
	 		holds the number of enemies currently in the game
		attack_towers : list(int)
			holds a list of all of the attack towers
	 	support_towers : list(int)
			holds a list of all of the support towers
	  lives : int
	 		the number of lives the player has
		money : int
			the amount of money the player starts with
		bg : str
			The picture of the main menu, scaled
	  timer : int
	 		The amount of time the game has been running for
	  life_font : str
	 		Font of everything
		selected_tower : boolean 
			If the user selects a tower then the variable will be true
	 		Else the variabnle is None
		menu.add_button : str
			picture of the button of the tower with the price of it
	 moving_object: boolean
			If the enemy is moving then this variable will be true
	 		Else the variable is None
		self.current_wave : int
			The current waves of enemies
	 	wave : into
	 		the current wave
		pause : boolean
			if true the game will be paused
	 		if false the game will not be paused
		music_on : boolean
			if true the music will be played
	 		if false the music will not be played	
		playPauseButton : int
			the placement of the playPause button
		soundButton : int
			the placement of the sound button	 	
	 	total_spend : str
	 		tracks users spending and puts it into a file
		
    Methods
    -------
    gen_enemies -> win
	    returns the enemy
		run -> none
			returns nothing
	 	point_to_line -> boolean
	 		if true you will be able to place tower
			if false you cannot place the tower
    draw() -> none
	    returns nothing
		'''
    def __init__(self, win, waves):
        '''
				Constructor to build a main menu obejct
			 
				Parameters
				----------
    		width : int
			    The width of the main menu 
			 	length : int
			 		The length of the main menu
				win : str
					used to draw picture
			 	enemys : list(int)
			 		holds the number of enemies currently in the game
				attack_towers : list(int)
					holds a list of all of the attack towers
			 	support_towers : list(int)
					holds a list of all of the support towers
			  lives : int
			 		the number of lives the player has
				money : int
					the amount of money the player starts with
				bg : str
					The picture of the main menu, scaled
			  timer : int
			 		The amount of time the game has been running for
			  life_font : str
			 		Font of everything
				selected_tower : boolean 
					If the user selects a tower then the variable will be true
			 		Else the variabnle is None
				menu.add_button : str
					picture of the button of the tower with the price of it
			 moving_object: boolean
					If the enemy is moving then this variable will be true
			 		Else the variable is None
				self.current_wave : int
					The current waves of enemies
			 	wave : into
			 		the current wave
				pause : boolean
					if true the game will be paused
			 		if false the game will not be paused
				music_on : boolean
					if true the music will be played
			 		if false the music will not be played	
				playPauseButton : int
					the placement of the playPause button
				soundButton : int
					the placement of the sound button	 	
			 	total_spend : str
			 		tracks users spending and puts it into a file
        '''
        self.width = 1350
        self.height = 700
        self.win = win
        self.enemys = []
        self.attack_towers = []
        self.support_towers = []
        self.lives = 10
        self.money = 200000
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_image.get_width() + 70, 250, side_image)
        self.menu.add_button(magicTower1, "magicTower1", 500)
        self.menu.add_button(magicTower2, "magicTower2", 750)
        self.moving_object = None
        self.wave = 0
        self.waves = waves
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.music_on = True
        self.playPauseButton = PlayPauseButton(play_button, pause_button, 10, self.height - 85)
        self.soundButton = PlayPauseButton(sound_button, sound_button_off, 90, self.height - 85)
        self.total_spend = 0

    def gen_enemies(self):
        '''
				generate the next enemy or enemies to show
			
				Returns
				------------------
				returns the enemies
        '''
        if sum(self.current_wave) == 0:
            if len(self.enemys) == 0:
              if self.wave < len(self.waves):
                self.wave += 1
                self.current_wave = self.waves[self.wave]
                self.pause = True
                self.playPauseButton.paused = self.pause
              else:
                print('The player has won')
                with open('leaderboard.txt', 'a') as file:
                    file.write(str(self.total_spend) + '\n')    
                pygame.quit()
        else:
            wave_enemies = [Goblin(), Orc(), Ogre()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def run(self):
        """
				starts the whole game
		
				Returns
				-------
				nothing
        """
        pygame.mixer.music.play(loops=-1)
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(500)

            if self.pause == False:
                # gen monsters
                if time.time() - self.timer >= random.randrange(1,6)/3:
                    self.timer = time.time()
                    self.gen_enemies()

            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # if you're moving an object and click
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_towers[:] + self.support_towers[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    else:
                        # check for play or pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause

                        if self.soundButton.click(pos[0], pos[1]):
                            self.music_on = not(self.music_on)
                            self.soundButton.paused = self.music_on
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # look if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.total_spend += cost
                                self.add_tower(side_menu_button)

                        # look if you clicked on attack tower or support tower
                        button_clicked = None
                        if self.selected_tower:
                            button_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if button_clicked:
                                if button_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        #total_spend += cost
                                        self.selected_tower.upgrade()

                        if not(button_clicked):
                            for tower_attack in self.attack_towers:
                                if tower_attack.click(pos[0], pos[1]):
                                    tower_attack.selected = True
                                    self.selected_tower = tower_attack
                                else:
                                    tower_attack.selected = False

                            # look if you clicked on support tower
                            for tower_attack in self.support_towers:
                                if tower_attack.click(pos[0], pos[1]):
                                    tower_attack.selected = True
                                    self.selected_tower = tower_attack
                                else:
                                    tower_attack.selected = False

            # loop through enemies
            if not self.pause: 
                to_delete = [] 
                for enemies_moving in self.enemys:
                    enemies_moving.move()
                    if enemies_moving.x > 1340:
                        to_delete.append(enemies_moving)

                # delete all enemies off the screen
                for d in to_delete:
                    self.lives -= 1
                    self.enemys.remove(d)

                # loop through attack towers
                for tower_attack in self.attack_towers:
                    self.money += tower_attack.attack(self.enemys)

                # loop through attack towers 
                for tower_attack in self.support_towers:
                    tower_attack.support(self.attack_towers)

                # if you lose
                if self.lives <= 0:
                    print("You Lose")
                    run = False

            self.draw()


    def point_to_line(self, tower):
        """
				Makes the game run, as well checking of the user won	
				
				Parameters
				----------
				Tower : boolean
			
				Returns: 
				------------------
        Boolean
  				If true user will be able to place tower
  				If false user will not be able to place tower
        """
        # find tower_attacko closest points
        return True

    def draw(self):
        """
				draws all of the things
		
				Parameters
				----------
				win: str
					parameters win: surface
		
				Returns
				-------
				nothing
        """
        self.win.blit(self.bg, (0,0))

        # draw placement rings
        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(self.win)

            for tower in self.support_towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

        # draw attack towers
        for tower_attack in self.attack_towers:
            tower_attack.draw(self.win)

        # draw support towers
        for tower_attack in self.support_towers:
            tower_attack.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        self.menu.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

        # draw music toggle button
        self.soundButton.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(lives_image,(50,50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(coin_image, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(money, (start_x, 65))

        # draw wave
        self.win.blit(wave_bg, (10,10))
        text = self.life_font.render("Wave #" + str(self.wave), 1, (255,255,255))
        self.win.blit(text, (10 + wave_bg.get_width()/2 - text.get_width()/2, 25))

        pygame.display.update()

    def add_tower(self, name):
        '''
				lets the user add a tower  from the object list
				
				Parameters
				----------
				name : str
					name of the tower
			
				Returns
				------------------
				nothing
        '''
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_magicTower1", "buy_magicTower2", "buy_damage", "buy_range"]
        object_list = [UpgradedMagicTower(x,y), SimpleMagicTower(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")