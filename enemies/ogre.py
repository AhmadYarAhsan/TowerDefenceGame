from .enemy import Enemy, enemyImgs

imgs = enemyImgs(5, 'ogre', (64,64))


class Ogre(Enemy):
    '''
    A child class that holds the name, the money earnt, the max hp and the picture of the Ogre.
		
    Attributes
    ----------
    Name : string
	    The name of the Ogre (Goblin)
	 	money : int
	 		The money earnt from killing the Ogre (25)
		max_health : int
			The max health of the Ogre
	 	imgs : str
	 		the picture of the Ogre
		'''
    def __init__(self):
        super().__init__()
        self.name = "Ogre"
        self.money = 100
        self.max_health = 100
        self.health = self.max_health
        self.imgs = imgs[:]


