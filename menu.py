import pygame
import os
pygame.font.init()

# Bringing logo assets over
star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "coin.png")).convert_alpha(), (50,50))
star2 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "coin.png")).convert_alpha(), (20,20))


class Button:
    '''
    Button class for menu objects
		
    Attributes
    ----------
    name : str
	    The name of the button 
    img : str
	    The picture of the button
    x : int
	    The x coordinate of the button
		y : int
	 		The y coordinate of the button
		 menu	: str
			it defines the menu
	 	width : int
	 		The width of the game
	  height : int
			The height of the game
    Methods
    -------
    click(x, y) -> none
	    returns if the positon has collided with the menu
    draw(win) -> none
	    draws the button image
    update() -> int
	    updates button position
		'''
    def __init__(self, menu, image, name):
        """
				Constructor build to build a button object
				
				Parameters
				----------
				menu : int
					where the menu is
				img : smth
					what the button looks like
				name : str
					The name of the object
				"""
        self.name = name
        self.image = image
        self.x = menu.x - 50
        self.y = menu.y - 110
        self.menu = menu
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def click(self, X, Y):
        """
				returns if the positon has collided with the menu
		
				Parameters
				----------
				x : int
					the x corodinate of the mouse when clicked
				y : int
					the y corodinate of the mouse when clicked 
		
				Returns
				-------
				bool
					True if the mouse was at a certain point
					False if the mouse was not at that point
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, win):
        """
        draws the button image
        :param win: surface
        :return: None
        """
        win.blit(self.image, (self.x, self.y))

    def update(self):
        """
				update the button button 
			
				Returns
				-------
				nothing
		
        """
        self.x = self.menu.x - 50
        self.y = self.menu.y - 110


class PlayPauseButton(Button):
    def __init__(self, play_image, pause_image, x, y):
        """
				Constructor build a play/pause button object
				
				Parameters
				----------
				pause_img : str
			    The picture of the pause button
				play_img : str
			    The picture of the play button
		    x : int
			    The x coordinate of the button
				y : int
				"""
        self.image = play_image
        self.play = play_image
        self.pause = pause_image
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.paused = True

    def draw(self, win):
        """
				redraws the button image
		
				Parameters
				----------
				win: str
					parameters win: surface
		
				Returns
				-------
				nothing
        """
        if self.paused:
            win.blit(self.play, (self.x, self.y))
        else:
            win.blit(self.pause, (self.x, self.y))


class VerticalButton(Button):
    """
    class for the vertical button in the main menu
		
    Attributes
    ----------
    name : str
	    The name of the button ()
    img : str
	    The picture of the button
    x : int
	    The x coordinate of the button
		y : int
	 		The y coordinate of the button
		 menu	: str
			it defines the menu
	 	width : int
	 		The width of the game
	  height : int
			The height of the game
	 cost : int
			The cost of the button in the menu
    """
	
    def __init__(self, x, y, image, name, cost):
			
        """
			Constructor build a vertical button object
			
			Parameters
			----------
			name : str
	    	The name of the button 
			img : str
				The picture of the button
			x : int
				The x coordinate of the button
			y : int
	 			The y coordinate of the button
	 		width : int
		 		The width of the game
		  height : int
				The height of the game
		 	cost : int
				The cost of the button in the menu
          """		
			
        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.cost = cost


class Menu:
    """
    menu for holding items
		
    Attributes
    ----------
    x : int
	    The x coordinate of the button
		y : int
	 		The y coordinate of the button
	 	width : int
	 		The width of the game
	  height : int
			The height of the game
	 item_cost : int
			The cost of the button in the menu
	 buttons : str
			List of all of the buttons on the main menu
	 items : int
	 	items added
	 bg : str
		picture of the background
	font :str
 		the font of the text
	tower : int
 		the number of towers the user has or uses
	 
    Methods
    -------
		add_btn : str
			adds buttons to menu
	 	get_item_cost : int
	 		gets cost of upgrade to next level
		draw : surface
			reutrns nothing
	 	get_clicked(X, Y) : int
	 		returns the name of the button
		update : none
			updates the button locatios
    """
    def __init__(self, tower, x, y, image, item_cost):
        """
			Constructor build a vertical button object
	 
			Parameters
			----------
			x : int
				The x coordinate of the button
			y : int
				The y coordinate of the button
			width : int
				The width of the game
			height : int
				The height of the game
			item_cost : int
				The cost of the button in the menu
			buttons : str
				List of all of the buttons on the main menu
			items : int
			items added
			bg : str
			picture of the background
			font :str
			the font of the text
			tower : int
			the number of towers the user has or uses
          """
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = image
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower 

    def add_button(self, image, name):
        """
				adds a buttons to the menu 
		
				Parameters
				----------
				img : str
					the image of the new button
				name : str
					the name of the new button
		 
				Returns
				-------
				nothing
        """
        self.items += 1
        self.buttons.append(Button(self, image, name))

    def get_item_cost(self):
        """
				gets cost of upgrade to next level
		
				Returns
				-------
				item_cost: int
					returns the cost of the tiem
        """
        return self.item_cost[self.tower.level - 1]

    def draw(self, win):
        """
				Draws the enemy with the given images
		
				Parameters
				----------
				 win: str
		 			surface
		
				Returns
				-------
				nothing        
				"""
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + item.width + 5, item.y-9))
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star.get_height() -8))

    def get_clicked(self, X, Y):
        """
				return the clicked item from the menu
		
				Parameters
				----------
				x : int
					The x coordinate of the button
				y : int
					The y coordinate of the button
			
				Returns
				-------
				the button name : str
        """
        for button in self.buttons:
            if button.click(X,Y):
                return button.name

        return None

    def update(self):
        """
				update menu and button location
			
				Returns
				-------
				nothing
		
        """
        for button in self.buttons:
            button.update()


class VerticalMenu(Menu):
    """
    class for the vertical menu for the side bar
		
    Attributes
    ----------
    x : int
	    The x coordinate of the button
		y : int
	 		The y coordinate of the button
	 	width : int
	 		The width of the game
	  height : int
			The height of the game
	 items : int
			The number of items 
	 bg : str
			Draws the button image and the background
	 buttons : list()
			appendeds all the buttons made to this list
    """
	
    def __init__(self, x, y, image):
        """
			Constructor build a vertical button object
	 
			Parameters
			----------
	    x : int
		    The x coordinate of the button
			y : int
		 		The y coordinate of the button
		 	width : int
		 		The width of the game
		  height : int
				The height of the game
		 items : int
				The number of items 
		 bg : str
				Draws the button image and the background
		 buttons : list()
				appendeds all the buttons made to this list
          """
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.buttons = []
        self.items = 0
        self.bg = image
        self.font = pygame.font.SysFont("comicsans", 25)

    def add_button(self, image, name, cost):
        """
				adds a buttons to the vertical menu 
		
				Parameters
				----------
				img : str
					the image of the new button
				name : str
					the name of the new button
		 		cost : int
		 			cost of the button
		 
				Returns
				-------
				nothing
        """
        self.items += 1
        button_x = self.x - 40
        button_y = self.y-100 + (self.items-1)*120
        self.buttons.append(VerticalButton(button_x, button_y, image, name, cost))

    def get_item_cost(self, name):
        """
				gets cost of the button
		
				Parameters
				----------
				name : str
					name of the button
	
				Returns: int
				------------
				item_cost: int
					returns the cost of the tiem
        """
        for button in self.buttons:
            if button.name == name:
                return button.cost
        return -1

    def draw(self, win):
        """
				Draws the enemy with the given images
		
				Parameters
				----------
				 win: str
		 			surface
		
				Returns
				-------
				nothing        
				"""
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)
            win.blit(star2, (item.x+2, item.y + item.height))
            text = self.font.render(str(item.cost), 1, (255,255,255))
            win.blit(text, (item.x + item.width/2 - text.get_width()/2 + 7, item.y + item.height + 5))




