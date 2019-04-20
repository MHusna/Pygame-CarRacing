import pygame
WHITE = (255, 255, 255)

# Bu sınıf bir arabayı temsil edicek.Sprite sınıfından türetildi.
class Car(pygame.sprite.Sprite):
	
	def __init__(self,color, width, height, speed):
		super().__init__()
		
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		
		self.width = width
		self.height = height
		self.color = color
		self.speed = speed
		
		
		
		pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
		
		#Bunun yerine uygun bir araba resmi yükleyebiliriz.
		# self.image = pygame.image.load("car.png").convert_alpha()
		
		# Resmin boyutlarına sahip olan dikdörtgen bir nesne alırız.
		self.rect = self.image.get_rect()
	
	def moveRight(self, pixels):
		self.rect.x += pixels
	
	def moveLeft(self, pixels):
		self.rect.x -= pixels
	
	def moveForward(self, speed):
		self.rect.y += (((self.speed)*speed) / 20)
	
	def moveBackward(self, speed):
		self.recy.y -= (((self.speed)*speed) / 20)
	
	def changeSpeed(self, speed):
		self.speed = speed
	
	def repaint(self, color):
		self.color = color
		pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
		
