import pygame
from src import die
from src import property
import random

class Player(pygame.sprite.Sprite):
  def __init__(self, filename='',name = '', x=0,y=0):
    '''Initializes a player object
    args: filename (str), name (str), x (int), y(int)'''
    super().__init__()
    self.image = pygame.image.load(filename).convert_alpha()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect() 
    self.rect.centerx = x 
    self.rect.centery = y
    self.name = name
    self.currentSpace = 0 
    self.money = 1500
    self.properties = []
    self.propNames = []
    self.stringOfProperties = ''

  def moveFromRoll(self, die1):
    '''Determines the new space for the player after the die has been rolled
    args: self (Player object), die1(Die object)'''
    self.currentSpace = self.currentSpace + die1.currentRoll
    if self.currentSpace > 19:
      self.currentSpace = self.currentSpace - 20

    

  def buyProperty(self, landedProperty):
    '''buy a property
    args: self (Player object), landedProperty (Property object)'''
    self.money -= landedProperty.value
    landedProperty.owner = self.name
    for i in self.properties:
      if landedProperty.color == i.color:
        landedProperty.rent = 5*landedProperty.rent
        i.rent = 5*i.rent
    self.properties.append(landedProperty)
    self.propNames.append(landedProperty.name)
    self.stringOfProperties += "*" + landedProperty.name
  
  def payRent(self, landedProperty, player2):
    '''pay rent function
    args: self, player 2 (Player objects), landedProperty (Property object)'''
    self.money -= landedProperty.rent
    player2.money += landedProperty.rent


  def chanceCard(self):
    '''returns a random number for a space that the player will go to.
    args: self (Player object)
    returns: int'''
    return random.randrange(0, 20)
    
    

  
  def communityChestCard(self):
    '''randomly adds or subtracts money from the player
    args: self (player object)'''
    self.money += random.randrange(-50,51)
    
  