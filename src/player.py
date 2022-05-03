import pygame
from src import die
from src import property
from src import utility
import random

class Player(pygame.sprite.Sprite):
  def __init__(self, filename='',name = '', x=0,y=0):
    '''Initializes a player object'''
    super().__init__()
    self.image = pygame.image.load(filename).convert_alpha()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect() 
    self.rect.x = x #center x of go space object
    self.rect.y = y#y coord for center of go space
    self.name = name
    self.currentSpace = 0 #number between 0 and total spaces
    self.money = 1500
    self.totalProperties = utility.Utility()
    self.totalProperties = self.totalProperties.tupleOfSpaces

  def moveFromRoll(self, die1):
    #Aviva's idea
    spaces = self.totalProperties
    self.currentSpace = self.currentSpace + die1.self.currentRoll
    if self.currentSpace > 19:
      self.currentSpace = self.currentSpace - 20
    newSpace = spaces[self.currentSpace]
    self.rect.x = newSpace.rect.x
    self.rect.y = newSpace.rect.y
    #each space on the board will have a dot/circle (this will be the image of each property or card object) - we can move the player to the exact coordinates of the dot, that way we don't have to worry about all the dots being the same distance from each other etc.. 
    
    # my idea
    # assign every property to a number
    # for example, if the third property on the board is named java, assign the number 3 with that property. Using the currentSpace feature and adding the die1 and die2 rolls, we would get a number which would be assigned to a certain property that we can now move the player to. We would get this number by adding currentspace, die1, and die2
    #property_number = self.currentSpace + die1.self.currentRoll + die2.self.currentRoll
    #sample code for the board being 7 by 7 and start being in top right corner and start coords being (0,0) These numbers can all be changed once we import the board
    #if property_number > 28
      #property_number = property_number - 28
    
    #if (property_number <= 7 and >0)
      #self.rect.x = 0
      #self.rect.y = 0 - property_number
    #elif (property_number <= 14 and property_number >= 8)
      #self.rect.y = -7
      #self.rect.x = 7 - property_number
    #elif (property_number <= 21 and property_number >= 15)
      #self.rect.x = -7
      #self.rect.y = property_number - 21
    #elif (property_number <=28 and property_number>= 22)
      #self.rect.y = 0
      #self.rect.x = property_number - 28
    
    
      
  #do we need this?
  def transferMoney(self,player2,money=0):
    '''transfer money between two players
    args: self, player2 (player objects), money (int)'''
    self.money -= money
    self.player2.self.money += money

  def buyProperty(self, landedProperty):
    '''buy a property
    args: self (player object), property (property object)'''
    self.money -= landedProperty.self.value
    property.self.owner = self.name

  def payRent(self, landedProperty, player2):
    '''pay rent function
    args: self, player 2 (player objects), '''
    self.money -= landedProperty.self.rent
    self.player2.self.money += landedProperty.self.rent

  def goToJail(self):
    jail = self.totalProperties[15]
    self.rect.x = jail.self.rect.x #make sure this is the right name!!!
    self.rect.y = jail.self.rect.y
    self.currentSpace = 15

  def chanceCard(self):
    '''randomly moves player to a space on the board
    args: self (card object), player (player object)'''
    space = random.randrange(0, 20)
    self.currentSpace = space
    newSpace = self.totalProperties[space]
    self.rect.x = newSpace.rect.x
    self.rect.y = newSpace.rect.y
    

  
  def communityChestCard(self):
    '''randomly adds or subtracts money from the player
    args: self (card object), player (player object)'''
    self.money += random.randrange(-50,51)
    
