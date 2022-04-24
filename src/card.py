class Card(pygame.sprite.Sprite):
  def __init__(self):
    '''Initializes a card
    args: self'''
    super().__init__(self)
    self.image
    self.rect = self.image.get_rect()
    self.chance = ''
    self.communityChest = ''
  def newChanceCard(self):
    '''gives a random action for a chance card
    args: self (card object)
    returns: self.change'''
    self.chance = 
    return self.chance

  def newCommunityChestCard(self):
    '''Gives a random action for a community chest card
    args: self (card object)
    returns: self.community chest'''
    self.communityChest =
    return self.communityChest