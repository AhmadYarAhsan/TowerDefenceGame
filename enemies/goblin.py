from .enemy import Enemy, enemyImgs

imgs = enemyImgs(5, 'goblin', (64,64))


class Goblin(Enemy):
    '''
    A child class that holds the name, the money earnt, the max hp and the picture of the goblin.
		
    Attributes
    ----------
    Name : string
	    The name of the goblin (Goblin)
	 	money : int
	 		The money earnt from killing the goblin (25)
		max_health : int
			The max health of the goblin
	 	imgs : str
	 		the picture of the goblin
		'''
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.money = 50
        self.max_health = 5
        self.health = self.max_health
        self.imgs = imgs
        self.speed_increase = 3



