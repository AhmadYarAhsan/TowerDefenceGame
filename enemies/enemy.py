import pygame
import math
import os


class Enemy:
    '''
    Enemy class for all of the enemies
		
    Attributes
    ----------
    img : str
	    The picture of the enemy
    x : int
	    The x coordinate of the enemy
		y : int
	 		The y coordinate of the enemy
	 	width : int
	 		The width of the game
	  height : int
			The height of the game
	 	animation_count : int
	 		The number of animations
		health : int
			The health of the user
	 	path : list(int)
	 		The path the goblins take
		path_pos: int
			The starting position of the enemies
	 	flipped : boolean
	 		checks to see if the enemies are on the other side of the tower, if true the tower will flip
		total_health : int
			Health of the enemies
	 	speed : int
	 		Speed of the enemies
 
    Methods
    -------
    draw(win) -> none
	    draws the enemy image
		draw_health_bar() -> int
			Draws health bar above the enemy
    click(x, y) -> boolean
			True if the enemy has been hit
			False if the enemy hasn't been hit
	 	move() -> int
	 		returns nothing
		hit(damage) -> boolean
			True if the user took damage
			False  if the user didnt took damaget
		'''
	
    def __init__(self):
    			
        '''
				Constructor to build a main menu obejct
			 
				Parameters
				----------
		    img : str
			    The picture of the enemy
		    x : int
			    The x coordinate of the enemy
				y : int
			 		The y coordinate of the enemy
			 	width : int
			 		The width of the game
			  height : int
					The height of the game
			 	animation_count : int
			 		The number of animations
				health : int
					The health of the user
			 	path : list(int)
			 		The path the goblins take
				path_pos: int
					The starting position of the enemies
			 	flipped : boolean
			 		checks to see if the enemies are on the other side of the tower, if true the tower will flip
				total_health : int
					Health of the enemies
			 	speed : int
			 		Speed of the enemies
        '''
			
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(549, 680), (442, 617), (274, 586), (163, 573), (116, 465), (124, 326), (163, 187), (257, 135), (372, 118), (508, 109), (655, 124), (787, 110), (907, 113), (999, 131), (1104, 158), (1198, 212), (1203, 275), (1134, 328), (1008, 364), (839, 344), (668, 363), (644, 459), (703, 560), (846, 576)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = pygame.transform.scale(
          pygame.image.load(os.path.join(
              "game_assets/enemies/goblin", "goblin0.png")),(64,64))
        self.dis=0
        self.path_pos=0
        self.move_count=0
        self.move_dis=0
        self.imgs=[]
        self.flipped=False
        self.max_health=0
        self.speed_increase=1.2

    def draw(self, win):
        """
				Draws the enemy with the given images
		
				Parameters
				----------
				param win: surface
		
				Returns
				-------
				nothing        
				"""
        self.img=self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width() /
                 2, self.y - self.img.get_height()/2 - 35))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
				Draws the health bar
		
				Parameters
		    ----------
				win: str
          
		
				Returns
				-------
				bool
					nothing
        """
        length=50
        move_by=round(length / self.max_health)
        health_bar=move_by * self.health

        pygame.draw.rect(win, (255, 0, 0),
                         (self.x-30, self.y-75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-30,
                         self.y - 75, health_bar, 10), 0)

    def collide(self, X, Y):
        """
				Checks to see if position has hit enemy
		
				Parameters
		    ----------
				x: int
          x coordinates of enemy
				y: int
          y coordinates of enemy
		
				Returns
				-------
				bool
					True if the enemy has been hit
					False if the enemy hasn't been hit
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False


    def hit(self, damage):
        """
				Checks to see if position has hit enemy
		
				Parameters
		    ----------
				damage : int
          damage caused from tower
		
				Returns
				-------
				bool
					True if the enemy has been hit
					False if the enemy hasn't been hit
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False

        self.x=self.path[0][0]
        self.y=self.path[0][1]
        self.img=None
        self.dis=0
        self.path_pos=0
        self.move_count=0
        self.move_dis=0
        self.imgs=[]
        self.flipped=False
        self.max_health=0

    def move(self):
        """
				
				Moves enemy around map
		
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
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count=0

        x1, y1=self.path[self.path_pos]
        x1=x1 + 75
        if self.path_pos + 1 >= len(self.path):
            x2, y2=((1350, 589))
        else:
            x2, y2=self.path[self.path_pos+1]

        x2=x2+75

        dirn=((x2-x1)*2, (y2-y1)*2)
        length=math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn=(dirn[0]/length * self.speed_increase,
              dirn[1]/length * self.speed_increase)

        if dirn[0] < 0 and not (self.flipped):
            self.flipped=True
            for x, img in enumerate(self.imgs):
                self.imgs[x]=pygame.transform.flip(img, True, False)

        move_x, move_y=((self.x + dirn[0]), (self.y + dirn[1]))

        self.x=move_x
        self.y=move_y

        # Using trig to find the shortest distance to next point
        if dirn[0] >= 0:  # moving right
            if dirn[1] >= 0:  # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:  # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1



def enemyImgs(numberOfImages, enemyName, size):
  """
  
  Gets the image assets for differnet enemies

  Parameters
  ----------
  numberOfImages: int
    number of assests the specfic enemey has
  enemyName: str
    name of specifc enemy
  size: tuple
    sets the size of the asset

  Returns
  -------
  nothing
  """
  imgs=[]
  for x in range(numberOfImages):
      add_str=str(x)
      imgs.append(pygame.transform.scale(
          pygame.image.load(os.path.join(
              f"game_assets/enemies/{enemyName}", f"{enemyName}{add_str}.png")),
      size))
  return imgs
