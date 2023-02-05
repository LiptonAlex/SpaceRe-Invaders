import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun): #пуля в позиції пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 12)
        self.color = 244, 66, 54
        self.speed = 3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self): #переміщення пулі
        self.y -= self.speed
        self.rect.y = self.y

    def drawing(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

