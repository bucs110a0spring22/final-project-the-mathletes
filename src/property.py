class Property(pygame.sprite.Sprite):
  def __init__(self, filename = '', x= 0, y=0, color= '', value = 0, rent = 0):
    '''initializes a property space on the board
    args: self, x, y (int)/float, filename (str), color (str), value, rent (ints)
    '''
    super().__init__(self)
    self.image = filename 
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.value = value
    self.color = color
    self.owner = None
    self.rent = rent

#go to jail - go to the jail space and lose $50