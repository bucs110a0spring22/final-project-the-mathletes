import pygame
import sys
import json
from src import die
from src import player
from src import property



class Controller:
  def __init__(self):
        pygame.init()
        self.width, self.height = 500, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250,250,250))
        self.board = pygame.image.load('assets/Board.jpg').convert_alpha()
        self.board = pygame.transform.scale(self.board, (500,500))
        self.blackSpace = pygame.image.load("assets/Black.png").convert()
        self.blackSpace = pygame.transform.scale(self.blackSpace, (500,100))
        pygame.font.init()
        self.properties = pygame.sprite.Group()
        self.player1 = player.Player(filename='assets/Shoe.jpg',name = 'Player 1', x=455,y=465)
        self.player2 = player.Player(filename='assets/Hat.jpg',name = 'Player 2', x=455,y=465)
        self.currentPlayer = self.player2
        self.otherPlayer = self.player1
        self.die = die.Die(img_file = 'assets/Die.png', x=250, y=330)
        fptr = open("assets/properties.json")
        properties = json.load(fptr)
        self.property_dictionary = {}
        for p in properties:
            new_property = property.Property(**p)
            self.properties.add(new_property)
            self.property_dictionary[new_property.name] = new_property
        self.all_sprites = pygame.sprite.Group((self.player1,) + (self.player2,) + tuple(self.properties), (self.die,))
        self.state = "STARTSCREEN"  
    
  def mainloop(self):

    while True:
        if(self.state == "STARTSCREEN"):
          self.menuloop()
        elif(self.state == "GAME"):
          self.gameloop()
        elif(self.state == "GAMEOVER"):
          self.gameoverloop()
  

  def menuloop(self):
      pygame.display.set_caption("Menu")
      while (self.state == "STARTSCREEN"):
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            self.state = "GAMEOVER"
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              self.state = "GAME"
            if event.key == pygame.K_q:
              pygame.quit()
              quit()
        
        self.background.fill((250,250,250))
        myfont = pygame.font.SysFont(None, 40)
        message1 = myfont.render('Computer Science Monopoly', True, (141,238,238))
        message2 = myfont.render('Press the space bar to start', True, (193,255,193))
        message3 = myfont.render('or press q to quit at any time.', True, (193,255,193))
        self.screen.blit(self.background, (self.width, self.height))
        self.screen.blit(message1, (50, 125))
        self.screen.blit(message2,(60, 190))
        self.screen.blit(message3,(60,230))
        pygame.display.flip()
      
  def gameloop(self):  
    pygame.display.set_caption("Monopoly")
    currentProperty = None
    #event loop
    while (self.state == "GAME"):
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            if self.currentPlayer == self.player1:
              self.currentPlayer = self.player2
              self.otherPlayer = self.player1
            elif self.currentPlayer == self.player2:
              self.currentPlayer = self.player1
              self.otherPlayer = self.player2
            self.die.rollDie()
            self.currentPlayer.moveFromRoll(self.die)
            currentProperty = self.properties.sprites()[self.currentPlayer.currentSpace]
            loop_once = 1
          if event.key == pygame.K_q:
              self.state = "GAMEOVER"
      if currentProperty and loop_once == 1:
        self.currentPlayer.rect.centerx = currentProperty.rect.x
        self.currentPlayer.rect.centery = currentProperty.rect.y
        p = currentProperty
        
        if p.name == 'Chance':
          newSpace = self.currentPlayer.chanceCard()
          self.currentPlayer.currentSpace = newSpace
          currentProperty = self.properties.sprites()[self.currentPlayer.currentSpace]
          self.currentPlayer.rect.centerx = currentProperty.rect.x
          self.currentPlayer.rect.centery = currentProperty.rect.y
        elif p.name == "Community Chest":
          self.currentPlayer.communityChestCard()
          loop_once = 0
        elif p.name == 'Just Visiting':
          pass
          loop_once = 0
        elif p.name == 'Free Parking':
          pass
          loop_once = 0
        elif p.name == 'Go To Jail':
          self.currentPlayer.rect.centerx = self.property_dictionary['Just Visiting'].rect.x
          self.currentPlayer.rect.centery = self.property_dictionary['Just Visiting'].rect.y
          self.currentPlayer.currentSpace = 5
          self.currentPlayer.money -= 50
          loop_once = 0
        elif p.name == 'Go':
          self.currentPlayer.money += 200
          loop_once = 0
        elif p.owner == None and (self.currentPlayer.money> p.value):
          self.currentPlayer.buyProperty(p)
          loop_once = 0
        elif p.owner != self.currentPlayer.name and p.owner != None: 
          self.currentPlayer.payRent(p, self.otherPlayer)
          loop_once = 0
      myfont = pygame.font.SysFont(None, 20)
      message4 = myfont.render(f'Press the spacebar to roll. The current roll is {self.die.currentRoll}', True, (0, 0, 0))
      message5 = myfont.render(f"Player 1 (Shoe): ${self.player1.money} Player 2 (Hat): ${self.player2.money}", True, (0, 0, 0))
      message6 = myfont.render(f'Shoe: {self.player1.stringOfProperties}', True, (250, 250, 250))
      message7 = myfont.render(f'Hat: {self.player2.stringOfProperties}', True, (250, 250, 250))
      self.screen.blit(self.board, (0,0))
      self.screen.blit(self.blackSpace,(0,500))
      self.screen.blit(message4,(100,400))
      self.screen.blit(message5,(100,100))
      self.screen.blit(message6,(20, 520))
      self.screen.blit(message7,(20, 550))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()
      if (self.player1.money <=0) or (self.player2.money <= 0):
        self.state = "GAMEOVER"

      print(self.player1.stringOfProperties)
      print(self.player2.stringOfProperties)
  def gameoverloop(self):
        self.background.fill((193,205,205))
        self.screen.blit(self.background, (0, 0))
        pygame.display.set_caption("Game Over")
        winner = ''
        if self.player1.money > self.player2.money:
          winner = "The winner is Player 1!"
        elif self.player1.money < self.player2.money:
          winner = "The winner is Player 2!"
        elif self.player1.money == self.player2.money:
          winner = "It's a tie!"
        myfont = pygame.font.SysFont(None, 25)
        message = myfont.render(f'Game Over. {winner}', True, (255,0,0))
        self.screen.blit(message, (100, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
