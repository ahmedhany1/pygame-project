import pygame

pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Setting the screen caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("E:\Downloads\project.png")
pygame.display.set_icon(icon)

# Creating the player
player_img = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480

def player():
    screen.blit(player_img, (player_x, player_y))

# Game loop
running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()