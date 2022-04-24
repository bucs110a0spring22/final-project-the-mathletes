import pygame
import random 
class Die(pygame.sprite.Sprite):
  def __init__(self, x = 0, y = 0):
    '''initializes a Die object'''
    super().__init__(self)
    self.currentRoll
    self.image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    

  def rollDie(self):
    '''function that 'rolls' a die
    args: self (die object)'''
    self.currentRoll = random.randrange(1,7)
    self.image = 
    #make a list of images and change image based on the roll
    def doubles(self, dieTwo):
      '''determines if doubles was rolled
      args: self, dieTwo (die object)'''
      if self.currentRoll == dieTwo.self.currentRoll:
        #tell the player to roll again
