import pygame, random

pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Setting the screen caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("E:\Downloads\project.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")

# Creating the player
player_img = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))


# Creating the enemy
enemy_img = pygame.image.load("alien.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(0, 50)
enemy_x_change = 4
enemy_y_change = 40

def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Bullet
bullet = pygame.image.load("bullet.png")
#player_x = 370
#player_y = 480
#player_x_change = 0


# Game loop
running = True

while running:

    # RGB
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0


    #
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    #
    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = 4
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -4
        enemy_y += enemy_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()