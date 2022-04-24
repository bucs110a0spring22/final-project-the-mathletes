import pygame
import property
class Player(pygame.sprite.Sprite):
  def __init__(self,name = ''):
    '''Initializes a player object'''
    super().__init__(self)
    self.image = 
    self.rect = self.image.get_rect() 
    self.rect.x = #center x of go space
    self.rect.y
    self.name
    self.money = 1500
    self.properties

  def move(self, direction):
  
  def transferMoney(self,player2,money=0):
    '''transfer money between two players
    args: self, player2 (player objects), money (int)'''
    self.money -= money
    player2.self.money += money

  def buyProperty(self, property):
    '''buy a property
    args: self (player object), property (property object)'''
    self.money -= property.self.value
    property.self.owner = self.name

  def payRent(self, property, player2):
    '''pay rent function
    args: self, player 2 (player objects), '''
    self.money -= property.self.rent
    player2.self.money += property.self.rent