import pygame
from .tower import Tower
import os
import math
from menu import Menu

# import assets for upgrade menu and buttons
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")).convert_alpha(), (120, 70))
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")).convert_alpha(), (50, 50))

# load simpe magic tower image
simple_image = []  
for x in range(16):
    simple_image.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/towers/simple", f"simple{x}.png")).convert_alpha(),
        (90, 90)))

# load simple magic tower projectile image
projectile_image = []
for i in range(5):
    projectile_image.append(pygame.image.load(os.path.join("game_assets", "projectile.png")).convert_alpha())


class SimpleMagicTower(Tower):
    '''
    A class that holds the name, range, effect, width, hegiht, price, and the picture of the tower.
		
    Attributes
    ----------
    Name : string
	    The name of the tower 
	 	range : int
	 		How far the tower can shoot
		max_health : int
			The max health of the Orc
	 	imgs : str
	 		the picture of the towers
		projectile_image : str
			the picture of the projectiles
	 	inRange : boolean
	 		If true returns that the enemy is in the range
			If false returns that the enemy is not in the range
	  damage : int
	 		the damage done by the turret

	
    Methods
    -------
    draw(win) -> int
	    checks the range of the tower
    change_range(win) -> int
	    changes the range of the tower
    attack() -> enemies
	    attacks an enemy in the enemy list, modifies the list
    upgrade() -> none
	    upgrades tower damage

    move(x, y) -> none
	    draws the range of the tower before placing
		'''
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_image = simple_image[:]
        self.projectile_image = projectile_image
        self.counting = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "archer"
        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, 5000,"MAX"])
        self.menu.add_button(upgrade_button, "Upgrade")

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win):
        """
				Draws the tower image
		
				Parameters
				----------
				 win: str
           surface
		
				Returns
				-------
				counting : int
        """
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving:
            self.counting += 1
            if self.counting >= len(self.projectile_image) * 10:
                self.counting = 0
        else:
            self.counting = 0

    def change_range(self, r):
        """
				Change range of archer tower
		
				Parameters
				----------
				 r: int
           the radius of the tower's range
		
				Returns
				-------
				nothing
        """
        self.range = r

    def attack(self, enemies):
        """
				attacks an enemy in the enemy list, modifies the list
		
				Parameters
				----------
				 enemies: int
           list of enemies
		
				Returns
				-------
				money : int
					returns money made from hitting enemies
        """
			
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y


            dis = math.sqrt((self.x - enemy.img.get_width()/2 - x)**2 + (self.y -enemy.img.get_height()/2 - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if first_enemy.hit(self.damage) == True:
                money = first_enemy.money * 2
                enemies.remove(first_enemy)
                print("Enemy has been hit")
          
        return money

# load upgraded magic tower images
upgraded_image = []
for x in range(16):
    upgraded_image.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/towers/upgraded", f"upgraded{x}.png")),
        (90, 90)))

# Load upgraded magic tower projectile images
upgraded_projectile_image = []
for i in range(5):
    upgraded_projectile_image.append(pygame.image.load(os.path.join("game_assets", "projectile.png")))


class UpgradedMagicTower(SimpleMagicTower):
    '''
    upgrade of the simple tower
		
    Attributes
    ----------
		name : str
			name of the upgraded tower(UpgradedMagicTower)
    tower_image : str
	    The image of the upgraded tower 
    projectile_image : str
	    The picture of the projectiles for the upgraded tower
		range : int
	 		the range of the tower
	 	inRange : boolean
	 		If true returns that the enemy is in the range
			If false returns that the enemy is not in the range
	  damage : int
			The damage of the updated tower
	 	menu : str
	 		The menu
		
 
		'''
    def __init__(self, x,y):
        super().__init__(x, y)
        self.tower_image = upgraded_image
        self.projectile_image = upgraded_projectile_image
        self.counting = 0
        self.range = 120
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage
        self.menu = Menu(self, self.x, self.y, menu_bg, [2500, 5500, "MAX"])
        self.menu.add_button(upgrade_button, "Upgrade")
        self.name = "UpgradedMagicTower"



