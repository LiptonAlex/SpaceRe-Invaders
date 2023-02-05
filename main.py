import pygame , Controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run ():
      pygame.init()
      screen = pygame.display.set_mode((700, 800))
      pygame.display.set_caption("Space Re-Invaders")
      pygame.display.set_icon(pygame.image.load("images/icon.bmp"))
      bg_color = (0, 0, 0)
      music = pygame.mixer.music.load('sounds/AceOfSpades.mp3')
      pygame.mixer.music.play(-1)
      gun = Gun(screen)
      bullets = Group()
      invs = Group()
      Controls.create_army(screen, invs)
      stats = Stats()
      sc = Scores(screen, stats)

      while True:
          Controls.events(screen, gun, bullets)
          if stats.run_game:
              gun.update_gun()
              bullets.update()
              Controls.update(bg_color, screen, gun, invs, bullets,  stats, sc)
              Controls.update_bullets(screen,stats, sc, invs, bullets)
              Controls.update_invs(stats, screen, sc, gun, invs, bullets)


run()