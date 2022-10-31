import pygame
import random
import math

pygame.init()  # initialise the pygame

screen = pygame.display.set_mode((800, 600))  # MAKES THE SCREEN

# TITLE AND ICON
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# ROCKET ICON
rocketImg = pygame.image.load('rocket.png')
x = 400
y = 500
a = 0

# ENEMY ICON
enemyImg = []
p = []
q = []
b = []
c = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    p.append(random.randint(10, 800))
    q.append(random.randint(0, 200))
    b.append(1)
    c.append(20)

# SCORE
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# GAME OVER
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
over_x = 325
over_y = 250

# BULLET ICON
bulletImg = pygame.image.load('bullet.png')
bullet_x = 0  # CHECK LINE No.68
bullet_y = 500
bullet_change_y = 8
bullet_state = "ready"  # SETS THE STATE OF BULLET as "ready" by default


# "ready" STATE MEANS BULLET WILL NOT APPEAR ON SCREEN

def rocket(x, y):
    screen.blit(rocketImg, (x, y))


def enemy(p, q, i):
    screen.blit(enemyImg[i], (p, q))


def bullet(bullet_x, bullet_y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (bullet_x, bullet_y))


def isCollision(p, q, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(p - bullet_x, 2)) + (math.pow(q - bullet_y, 2)))
    if distance <= 35:
        return True
    else:
        return False


def show_score(text_x, text_y):
    score1 = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score1, (text_x, text_y))


def game_over(over_x, over_y):
    over_font = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_font, (over_x, over_y))


# GAME LOOP
running = True
while running == True:  # TO KEEP SCREEN OPEN
    # COLOURING SCREEN=R,G,B
    screen.fill((0, 0, 0))
    for event in pygame.event.get():  # TO ACTIVATE CLOSE BUTTON
        if event.type == pygame.QUIT:
            running = False
        # KEYSTROKES CODING
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                a = -0.5
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                a = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    print("space bar is pressed")
                    bullet_x = x + 16
                    bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key Strokes has been released")
                a = 0
    # MOVEMENT OF ROCKET
    x += a
    if x >= 736:
        x = 736
    if x <= 0:
        x = 0
    # MOVEMENT OF ENEMY
    for i in range(num_of_enemies):
        p[i] += b[i]
        if p[i] >= 736:
            q[i] += c[i]
            p[i] = 736
            b[i] = -1
        if p[i] <= 0:
            q[i] += c[i]
            p[i] = 0
            b[i] = 1
        # COLLISION CODING
        if isCollision(p[i], q[i], bullet_x, bullet_y) is True:
            bullet_state = "ready"
            bullet_y = 500
            score += 1
            print(score)
            p[i] = random.randint(0, 800)
            q[i] = random.randint(0, 200)
        enemy(p[i], q[i], i)
        # GAME OVER CODING:
        if q[i] > 450:
            for j in range(num_of_enemies):
                q[j] = 4000
            game_over(over_x, over_y)
            break
    # MOVEMENT OF BULLET
    if bullet_state is "fire":
        bullet_y -= 1
        bullet(bullet_x, bullet_y)
    if bullet_y <= 0:
        bullet_y = 500
        bullet_state = "ready"

    rocket(x, y)
    show_score(text_x, text_y)
    pygame.display.update()
pygame.quit()
