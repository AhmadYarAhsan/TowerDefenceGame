import pygame
from menu import Menu
import os
import math

# Setting up menus for towers
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")).convert_alpha(), (120, 70))
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")).convert_alpha(), (50, 50))


class Tower:
    '''
    A class that holds the x, y, animation count, width, hegiht, sell price, price, level, selected, menu, pictures of the tower, and placement colour.
		
    Attributes
    ----------
    x : int
	    The x coordinate of the tower
		y : int
	 		The y coordinate of the tower
		animation_count	: int
			number of pictures needed to animate
	 	width : int
	 		The width of the game
	  height : int
			The height of the game
    sell_price : int
      Money earned to sell tower
    price : int
      Money required to buy the tower
    level : int
      d
    selected : bool
      Checking to see if tower is clicked
    menu : list
      d
    tower_imgs : list
      Images of tower
    damage : int
      Damage output on enemies
    place_colour : int
      Red circle showing the range of the tower

    Methods
    -------
    click(x, y) -> none
	    returns if the positon has collided with the menu
    draw(win) -> none
	    draws the tower image
    draw_radius(win) -> none
	    draws the range of the tower
    draw_placement(win) -> none
	    draws the range of the tower before placing
    sell() -> int
	    gives price of tower if sold
    upgrade() -> none
	    upgrades tower damage
    get_upgrade_cost() -> int
	    shows the upgrade cost
    move(x, y) -> none
	    draws the range of the tower before placing
		'''
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_cost = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.selected = False
        # define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, "MAX"])
        self.menu.add_button(upgrade_button, "Upgrade")

        self.tower_image = []
        self.damage = 1

        self.place_color = (0,0,255, 100)

    def draw(self, win):
        """
				
				Draws the tower image
		
				Parameters
				----------
				 win: str
           surface
		
				Returns
				-------
				nothing
        """
        img = self.tower_image[self.level - 1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

        # draw menu
        if self.selected:
            self.menu.draw(win)

    def draw_radius(self,win):
        """
				
				Draws the range of the tower while running
		
				Parameters
				----------
				 win: str
           surface
		
				Returns
				-------
				nothing
        """
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self,win):

        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, X, Y):
        """
				
				Checks to see if tower is clicked on
		
				Parameters
				----------
				x: int
          x coordinate 
        Y: int
          y coordinate
		
				Returns
				-------
				bool
					True if the mouse was at a certain point
					False if the mouse was not at that point
        """
        img = self.tower_image[self.level - 1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False

    def sell(self):
        """
				
				Sells the tower for money
		
				Returns
				-------
				int
					Price of the sold tower
        """
        return self.sell_cost[self.level-1]

    def upgrade(self):
        """
				
				Upgrades tower to do more damage
		
				Returns
				-------
			  nothing
        """
        if self.level < len(self.tower_image):
            self.level += 1
            self.damage += 1

    def get_upgrade_cost(self):
        """
				
				Displays cost of tower upgrade
		
				Returns
				-------
			  int
          Price of upgrade
        """
        return self.price[self.level-1]

    def move(self, x, y):
        """
				
				Moves tower around map
		
				Parameters
				----------
				x: int
          x coordinate 
        Y: int
          y coordinate
		
				Returns
				-------
				nothing
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, otherTower):
        """
				
				Checks to see if tower is to close to another
		
				Parameters
				otherTower: int
          coordinates of aleardy placed tower 

		
				Returns
				-------
				bool
					True if the tower was too close to other tower
					False if the tower was not to close to other tower
        """
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True


