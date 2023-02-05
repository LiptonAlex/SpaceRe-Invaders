import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():

    def __init__(self, screen, stats): #init of score recording
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (244, 66, 54)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_health()

    def image_score(self): #making text to score image
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 50
        self.score_rect.top = 30

    def image_high_score(self): #making high score to img
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self): #score showing
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.healths.draw(self.screen)

    def image_health(self): #health counter
        self.healths = Group()
        for health_number in range(self.stats.guns_left):
            health = Gun(self.screen)
            health.rect.x = 500 + health_number * health.rect. width
            health.rect.y = 20
            self.healths.add(health)
