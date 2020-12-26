import pygame
import random

# Initialising pygame
pygame.init()

# Creating a screen
screen = pygame.display.set_mode((800, 600))

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
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

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
                fire_bullet(playerX, bulletY)

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
    enemyX+=enemyX_change

    # Setting boundries for enemy
    if enemyX<=0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX>736:
        enemyX_change = -4
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Bullet Movement
    if bulletState is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    # Update the game window always
    pygame.display.update()
