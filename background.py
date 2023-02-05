import pygame

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/background.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def output(self):
        self.screen.blit(self.image, self.rect)