import pygame
import sys
import random
from src import die
from src import player
from src import property
from src import button
from src import utility
#change all properties to self.tupleOfSpces
class Controller:
  def __init__(self, width=500, height=500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250,250,250))  # set the background to green
        self.board = pygame.image.load('assets/Board.jpg').convert_alpha()
        pygame.font.init()
        self.properties = pygame.sprite.Group()
        self.player1 = player.Player(filename='assets/Shoe.jpg',name = 'Player 1', x=0,y=0)
        self.player2 = player.Player(filename='assets/Hat.jpg',name = 'Player 2', x=0,y=0)
        self.currentPlayer = self.player2
        self.otherPlayer = self.player1
        self.die = die.Die(img_file = 'assets/Die.jpg', x=250, y=330) 
        self.properties.add(property.Property(name = 'Go', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0))
        self.properties.add(property.Property(name = 'Fortran', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Black', value = 30, rent = 4))
        self.properties.add(property.Property(name = 'Swift', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Black', value = 60, rent = 6))
        self.properties.add(property.Property(name = 'Groovy', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Light Blue', value = 80, rent = 10))
        self.properties.add(property.Property(name = 'Ruby', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Light Blue', value = 100, rent = 12))
        self.properties.add(property.Property(name = 'Just Visiting', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0))
        self.properties.add(property.Property(name = 'SQL', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Pink', value = 120, rent = 16))
        self.properties.add(property.Property(name = 'PHP', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Pink', value = 150, rent = 20))
        self.properties.add(property.Property(name = 'Chance', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0))
        self.properties.add(property.Property(name = 'R', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Red', value = 180, rent = 25))
        self.properties.add(property.Property(name = 'Free Parking', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0))
        self.properties.add(property.Property(name = 'Go lang', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Red', value = 210, rent = 35))
        self.properties.add(property.Property(name = 'JavaScript', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Yellow', value = 230, rent = 40))
        self.properties.add(property.Property(name = 'HTML', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Yellow', value = 260, rent = 45))
        self.properties.add(property.Property(name = 'Community Chest', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0))
        self.properties.add(property.Property(name = 'Go To Jail', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0))
        self.properties.add(property.Property(name = 'C', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Green', value = 300, rent = 60))
        self.properties.add(property.Property(name = 'C++', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Green', value = 320, rent = 70))
        self.properties.add(property.Property(name = 'Java', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Blue', value = 350, rent = 80))
        self.properties.add(property.Property(name = 'Python', filename = 'assets/Man.jpg', x= 0, y=0, color= 'Blue', value = 500, rent = 100))
        self.all_sprites = pygame.sprite.Group((self.player1,) + (self.player2,) + tuple(self.properties), (self.die,))
        self.state = "STARTSCREEN"  
    #setup pygame data
    
  def mainloop(self):
    #select state loop
    while True:
            if(self.state == "STARTSCREEN"):
              self.menuloop()
            elif(self.state == "GAME"):
                self.gameoop()
            elif(self.state == "GAMEOVER"):
                self.gameverloop()
  
  ### below are some sample loop states ###

  def menuloop(self):
      while (self.state == "STARTSCREEN"):

        #put messages with instructions on how to play
        #start_button = button(self.screen, (500, 300), "Start (2 player game)")
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              self.state = "GAME"
              #self.screen.blit(self.board, (self.width, self.height)) 
              #self.all_sprites.draw(self.screen)
              #pygame.display.flip()
            if event.key == pygame.K_q:
              pygame.quit()
              quit()
        self.background.fill((250,250,250))
        myfont = pygame.font.SysFont(None, 40)
        message1 = myfont.render('Computer Science Monopoly', False, (0,139,139))
        message2 = myfont.render('Press the space bar to start', False, (0, 0, 0))
        message3 = myfont.render('or press q to quit.', False, (0, 0, 0))
        self.screen.blit(self.background, (self.width, self.height))
        self.screen.blit(message1, (50, 125))
        self.screen.blit(message2,(60, 160))
        self.screen.blit(message3,(110,200))
        pygame.display.flip()
        pygame.display.update()#do we need flip and update?  
            #if event.type == pygame.MOUSEBUTTONDOWN():
            #if start_button.collidepoint(pygame.mouse.get_pos()):
              #self.state = "GAME"
      #event loop

      #update data

      #redraw
      
      
  def gameloop(self):
    myfont = pygame.font.SysFont(None, 20)  
    #event loop
    while self.state == "GAME":
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN():
          if self.die.collidepoint(pygame.mouse.get_pos()):
            if self.currentPlayer == self.player1:
              self.currentPlayer = self.player2
              self.otherPlayer = self.player1
            elif self.currentPlayer == self.player2:
              self.currentPlayer = self.player1
              self.otherPlayer = self.player2
            self.die.rollDie()
            self.currentPlayer.moveFromRoll(self.die)
            currentProperty = pygame.sprite.spritecollide(self.currentPlayer,             self.properties, True) #do you have to add it back to the group?
          
        if currentProperty:
          for p in currentProperty:
            if p.self.name == 'Chance':
              self.currentplayer.chanceCard()
            elif p.self.name == "Community Chest":
              self.currentplayer.communityChestCard()
            elif p.self.name == 'Just Visiting':
              pass
            elif p.self.name == 'Free parking':
              pass
            elif p.self.name == 'Go To Jail':
              self.currentPlayer.goToJail()
            elif p.self.name == 'Go':
              self.currentPlayer.self.money += 200
            elif p.self.owner == None and (self.currentPlayer.self.money>= p.self.value):
              self.currentPlayer.buyProperty()
            if p.self.owner != self.currentPlayer.self.name:
              self.currentPlayer.payRent(p, self.otherPlayer)

          
      #what happens if two player collide?      
      #update data

      #redraw 
      message4 = myfont.render('Press the die to roll', False, (0, 0, 0))
      self.screen.blit(self.board, (self.width, self.height)) 
      self.screen.blit(message4,(200,400))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()
  
  
  def gameoverloop(self):
        #how do we make the whole screen blank?
        winner = ''
        if self.player1.self.money > self.player2.self.money:
          winner = "Player 1"
        elif self.player1.self.money < self.player2.self.money:
          winner = "Player 2"
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
    #event loop

      #update data

      #redraw
