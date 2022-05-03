import pygame
from src import property
class Utility(pygame.sprite.Sprite):
  
  def __init__(self):
    super().__init__()
    self.space0 = property.Property(name = 'Go', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0)
    self.space1 = property.Property(name = 'Fortran', filename = 'assets/Man.jpg', x= 0, y=0, color= "Black", value = 30, rent = 4)
    self.space2 = property.Property(name = 'Swift', filename = 'assets/Man.jpg', x= 0, y=0, color= "Black", value = 60, rent = 6)
    self.space3 = property.Property(name = 'Groovy', filename = 'assets/Man.jpg', x= 0, y=0, color= "Light Blue", value = 80, rent = 10)
    self.space4 = property.Property(name = 'Ruby', filename = 'assets/Man.jpg', x= 0, y=0, color= "Light Blue", value = 100, rent = 12)
    self.space5 = property.Property(name = 'Just Visiting', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0)
    self.space6 = property.Property(name = 'SQL', filename = 'assets/Man.jpg', x= 0, y=0, color= "Pink", value = 120, rent = 16)
    self.space7 = property.Property(name = 'PHP', filename = 'assets/Man.jpg', x= 0, y=0, color= "Pink", value = 150, rent = 20)
    self.space8 = property.Property(name = 'Chance', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0)
    self.space9 = property.Property(name = 'R', filename = 'assets/Man.jpg', x= 0, y=0, color= "Red", value = 180, rent = 25)
    self.space10 = property.Property(name = 'Free Parking', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0)
    self.space11 = property.Property(name = 'Go lang', filename = 'assets/Man.jpg', x= 0, y=0, color= "Red", value = 210, rent = 35)
    self.space12 = property.Property(name = 'JavaScript', filename = 'assets/Man.jpg', x= 0, y=0, color= "Yellow", value = 230, rent = 40)
    self.space13 = property.Property(name = 'HTML', filename = 'assets/Man.jpg', x= 0, y=0, color= "Yellow", value = 260, rent = 45)
    self.space14 = property.Property(name = 'Community Chest', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0)
    self.space15 = property.Property(name = 'Go To Jail', filename = 'assets/Man.jpg', x= 0, y=0, color= None, value = 0, rent = 0)
    self.space16 = property.Property(name = 'C', filename = 'assets/Man.jpg', x= 0, y=0, color= "Green", value = 300, rent = 60)
    self.space17 = property.Property(name = 'C++', filename = 'assets/Man.jpg', x= 0, y=0, color= "Green", value = 320, rent = 70)
    self.space18 = property.Property(name = 'Java', filename = 'assets/Man.jpg', x= 0, y=0, color= "Blue", value = 350, rent = 80)
    self.space19 = property.Property(name = 'Python', filename = 'assets/Man.jpg', x= 0, y=0, color= "Blue", value = 500, rent = 100)
    self.tupleOfSpaces = (self.space0, self.space1,self.space2,self.space3,self.space4,self.space5,self.space6,self.space7,self.space8,self.space9,self.space10,self.space11,self.space12,self.space13,self.space14,self.space15,self.space16,self.space17,self.space18,self.space19)
