import pygame
import random
import math
from pygame import mixer
# Initialising pygame
pygame.init()

# Creating a screen
screen = pygame.display.set_mode((800, 600))

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

#Background
background = pygame.image.load("background.png")
#Title and icon
pygame.display.set_caption("Space Invaders ")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    # blit = draw {blit(image, (x, y))}
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg, enemyY, enemyX, enemyX_change, enemyY_change = [], [], [], [], []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bulletState = "ready"

def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX), 2) +  (math.pow((enemyY-bulletY), 2)))
    if distance < 27:
        return True
    return False

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check wheter righ or left

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            
            if event.key == pygame.K_SPACE:
                if bulletState == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    playerX+=playerX_change
    # Setting boundries for player
    if playerX<=0:
        playerX = 0
    elif playerX>736:
        playerX = 736
    
    # Enemy Movement
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i]>440:
            final_score = game_over_font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(background, (0,0))
            screen.blit(final_score, (200, 250))
            show_score(textX, textY)
            break
        enemyX[i]+=enemyX_change[i]

        # Setting boundries for enemy
        if enemyX[i]<=0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

          # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bulletState = 'ready'
            score_value+=1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)

    # Bullet Movement
    ## Resetting bullet
    if bulletY<=0:
        bulletState = 'ready'
        bulletY = 480

    if bulletState == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
  
    show_score(textX, textY)

    # Update the game window always
    pygame.display.update()
