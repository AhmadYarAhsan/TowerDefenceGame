class Button():
	'''
    Button class for main menu objects
		
    Attributes
    ----------
    img : str
	    The picture of the button
    x_pos : int
	    The x coordinate of the button
		y_pos : int
	 		The y coordinate of the button
		font : str
			the font of the text
	  base_colour , hovering_colour : int
	 		the color of the objects
		text_input : str
			text that needs to be displayed
	 	rect: tuple
	 		the outline of the button
		text_rect: tuple
			the text inside 			
			
    Methods
    -------
    changeColor(position) -> none
	    changes the color of the button
    checkForInput() -> boolean
	    returns nothing
    update(screen) -> none
	    updates the screen 
  '''
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		'''
		
		Constructor build to build a button object
		
		Parameters
		----------
			img : str
				The picture of the button
			x_pos : int
				The x coordinate of the button
			y_pos : int
				The y coordinate of the button
			font : str
				the font of the text
			base_colour , hovering_colour : int
				the color of the objects
			text_input : str
				text that needs to be displayed
			rect: tuple
				the outline of the button
			text_rect: tuple
				the text inside
	  '''
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		'''
		updates the screeen
	
		parameters
		------------
		screen : int
	
		Returns
		-------
		nothing
    '''
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		'''
		checks for input of the mouse
	
		parameters
		------------
		position : int
	
		Returns:
		-----------------
		nothing
	  '''
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		'''
		changes the color in accordence to the mouse
	
		parameters
		------------
		position : int
	
		Returns: 
		-----------------
		nothing
	  '''
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)