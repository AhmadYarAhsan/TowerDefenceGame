from .enemy import Enemy, enemyImgs

imgs = enemyImgs(22, 'orc', (64,64))

class Orc(Enemy):
    '''
   A child class that holds the name, the money earnt, the max hp and the picture of the Orc.
		
    Attributes
    ----------
    Name : string
	    The name of the Orc (Goblin)
	 	money : int
	 		The money earnt from killing the Orc (25)
		max_health : int
			The max health of the Orc
	 	imgs : str
	 		the picture of the Orc
		'''
    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.money = 400
        self.imgs = imgs
        self.max_health = 200
        self.health = self.max_health
        self.speed_increase = 8




