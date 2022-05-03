import pygame
import random 
from src import player
from src import player
class Die(pygame.sprite.Sprite):
  def __init__(self, img_file = '', x=0, y=0):
    '''initializes a Die object'''
    super().__init__()
    self.currentRoll = 0
    self.image = pygame.image.load(img_file).convert_alpha()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    

  def rollDie(self):
    '''function that 'rolls' a die
    args: self (die object)'''
    self.currentRoll = random.randrange(1,7)
    
