import pygame, sys
from bullet import Bullet
from invaders import Inv
import time


def events(screen, gun, bullets):      #enevnts processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.moveright = True
            elif event.key == pygame.K_LEFT:
                gun.moveleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                gun_shot = pygame.mixer.Sound('sounds/blaster.mp3')
                gun_shot.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.moveright = False
            elif event.key == pygame.K_LEFT:
                gun.moveleft = False

def update(bg_color, screen, gun, invs, bullets, stats, sc):  #drawing
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.drawing()
    gun.output()
    invs.draw(screen)
    pygame.display.flip()

def update_bullets(screen,stats, sc, invs, bullets): #updating bullets position
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, invs, True, True)
    if collisions:
        for invs in collisions.values():
            stats.score += 1 * len(invs)
        sc.image_score()
        check_high_scores(stats, sc)
        sc.image_health()
    if len(invs) == 0:
        bullets.empty()
        create_army(screen, invs)

def gun_kill(stats, screen, sc, gun, invs, bullets): #gun collission with invaders
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_health()
        invs.empty()
        bullets.empty()
        create_army(screen, invs)
        gun.create_gun()
        time.sleep(1)
    else:
        dead_sound = pygame.mixer.Sound('sounds/loose.mp3')
        dead_sound.play()
        stats.run_game = False
        print("You  Loose!")
        time.sleep(1)
        sys.exit()

def update_invs(stats, screen, sc, gun, invs, bullets): #updating invaders location
    invs.update()
    if pygame.sprite.spritecollideany(gun, invs):
        gun_kill(stats, screen, sc, gun, invs, bullets)
    invs_check(stats, screen, sc, gun, invs, bullets)



def invs_check(stats, screen, sc, gun, invs, bullets): #check invaders on screenborder
    screen_rect = screen.get_rect()
    for inv in invs.sprites():
        if inv.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, invs, bullets)
            break


def create_army(screen, invs): #creating invaders army
    inv = Inv(screen)
    inv_width = inv.rect.width
    number_inv_x = int((700 - 2 * inv_width) / inv_width)
    inv_height = inv.rect.height
    number_inv_y = int((600 - 300 - 2 * inv_height) / inv_height)

    for row_number in range(number_inv_y):
        for inv_number in range(number_inv_x):
            inv = Inv(screen)
            inv.x = inv_width + (inv_width * inv_number)
            inv.y = inv_height + (inv_height * row_number)
            inv.rect.x = inv.x
            inv.rect.y = inv.rect.height + (inv.rect.height * row_number)
            invs.add(inv)

def check_high_scores(stats, sc): #high-score checking
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))

def draw_text(text, font, text_color, x, y):
    pygame.font.init()
    font = pygame.font.SysFont('calibri', 40)
    text_color = (255, 255, 255)
    screen = pygame.display.set_mode((700, 800))
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

