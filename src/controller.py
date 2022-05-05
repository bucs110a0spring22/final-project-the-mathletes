import pygame
import sys
import json
from src import die
from src import player
from src import property


#change all properties to self.tupleOfSpces
class Controller:
  def __init__(self):
        pygame.init()
        self.width, self.height = 500, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250,250,250))  # set the background to white
        self.board = pygame.image.load('assets/Board.jpg').convert_alpha()
        self.board = pygame.transform.scale(self.board, (500,500))
        pygame.font.init()
        self.properties = pygame.sprite.Group()
        self.player1 = player.Player(filename='assets/Shoe.jpg',name = 'Player 1', x=455,y=465)
        self.player2 = player.Player(filename='assets/Hat.jpg',name = 'Player 2', x=455,y=465)
        self.currentPlayer = self.player2
        self.otherPlayer = self.player1
        self.die = die.Die(img_file = 'assets/Die.jpg', x=250, y=330)
        fptr = open("assets/properties.json")
        properties = json.load(fptr)
        self.property_dictionary = {}
        for p in properties:
            new_property = property.Property(**p)
            self.properties.add(new_property)
            self.property_dictionary[new_property.name] = new_property
            #self.properties.add(property.Property(name=p['name'], filename=p['filename']))
        self.all_sprites = pygame.sprite.Group((self.player1,) + (self.player2,) + tuple(self.properties), (self.die,))
        self.state = "STARTSCREEN"  
    #setup pygame data
    
  def mainloop(self):
    #select state loop
    #put a string for current roll
    while True:
        if(self.state == "STARTSCREEN"):
          self.menuloop()
        elif(self.state == "GAME"):
          self.gameloop()
        elif(self.state == "GAMEOVER"):
          self.gameoverloop()
  
  ### below are some sample loop states ###

  def menuloop(self):
      pygame.display.set_caption("Menu")
      while (self.state == "STARTSCREEN"):
        
        #put messages with instructions on how to play
        #start_button = button(self.screen, (500, 300), "Start (2 player game)")
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            self.state = "GAMEOVER"
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
        message2 = myfont.render('Press the space bar to start', False, (250, 0, 0))
        message3 = myfont.render('or press q to quit at any time.', False, (0, 250, 0))
        self.screen.blit(self.background, (self.width, self.height))
        self.screen.blit(message1, (50, 125))
        self.screen.blit(message2,(60, 160))
        self.screen.blit(message3,(110,200))
        pygame.display.flip()
        #pygame.display.update()#do we need flip and update?  
            #if event.type == pygame.MOUSEBUTTONDOWN():
            #if start_button.collidepoint(pygame.mouse.get_pos()):
              #self.state = "GAME"
      #event loop

      #update data

      #redraw
      
      
  def gameloop(self):
  #get_rect. or rect.   
    pygame.display.set_caption("Monopoly")
    plist = self.properties.sprites()
    currentProperty = None
    #event loop
    while (self.state == "GAME"):
      #currentProperty = None
      for event in pygame.event.get():
        #if event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
          #if self.die.rect.collidepoint(pygame.mouse.get_pos()):
            if self.currentPlayer == self.player1:
              self.currentPlayer = self.player2
              self.otherPlayer = self.player1
            elif self.currentPlayer == self.player2:
              self.currentPlayer = self.player1
              self.otherPlayer = self.player2
            #plist = self.properties.sprites() - should this be on top?
            self.die.rollDie()
            self.currentPlayer.moveFromRoll(self.die)
            currentProperty = self.properties.sprites()[self.currentPlayer.currentSpace]
            #self.currentPlayer.currentSpace = (self.currentPlayer.currentSpace + self.die.currentRoll) % len(plist)
            #currentProperty = self.properties.sprites()[(self.die.currentRoll + self.currentPlayer.currentSpace)% len(plist)]
            #self.currentPlayer.moveFromRoll(self.die)
            #currentProperty = pygame.sprite.spritecollide(self.currentPlayer,             self.properties, True) #do you have to add it back to the group?
        # I think we have to set up the sprite groupes in the controller before we define this method. We have the one for properties but may need to make one for currentplayer
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_q:
              #self.state = "GAMEOVER"

    # if there is a collision, col is a list of properties collided with
      if currentProperty:
        self.currentPlayer.rect.x = currentProperty.rect.x
        self.currentPlayer.rect.y = currentProperty.rect.y
        p = currentProperty
        if p.name == 'Chance':
          newSpace = self.currentPlayer.chanceCard()
          self.currentPlayer.currentSpace = newSpace
          currentProperty = self.properties.sprites()[self.currentPlayer.currentSpace]
          self.currentPlayer.rect.x = currentProperty.rect.x
          self.currentPlayer.rect.y = currentProperty.rect.y
          
          
          
        elif p.name == "Community Chest":
          self.currentPlayer.communityChestCard()
        elif p.name == 'Just Visiting':
          pass
        elif p.name == 'Free parking':
          pass
        elif p.name == 'Go To Jail':
            self.currentPlayer.rect.x = self.properties_dictionary['jail'].rect.x
            self.currentPlayer.rect.y = self.properties_dictionary['jail'].rect.y
        elif p.name == 'Go':
          self.currentPlayer.money += 200
        elif p.owner == None and (self.currentPlayer.money>= p.value):
          self.currentPlayer.buyProperty(p)
        if p.owner != self.currentPlayer.name:
          self.currentPlayer.payRent(p, self.otherPlayer)
             
      #add event that will quit the game
              
      #what happens if two player collide?      
      #update data

      #redraw
      
      myfont = pygame.font.SysFont(None, 20)
      message4 = myfont.render('Press the spacebar to roll', False, (0, 0, 0))
      message5 = myfont.render(f"Player 1: ${self.player1.money}. Player 2: ${self.player2.money}", False, (0, 0, 0))
      self.screen.blit(self.board, (0,0)) 
      self.screen.blit(message4,(200,400))
      self.screen.blit(message5,(150,100))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()
  
  
  def gameoverloop(self):
        #how do we make the whole screen blank?
        self.background.fill((250,250,250))
        self.screen.blit(self.background, (0, 0))
        pygame.display.set_caption("Game Over")
        winner = ''
        if self.player1.money > self.player2.money:
          winner = "Player 1"
        elif self.player1.money < self.player2.money:
          winner = "Player 2"
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render(f'Game Over. The winner is {winner}', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
    #event loop

      #update data

      #redraw
