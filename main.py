import pygame
import json

from player import Player
from gun import Gun

# Constantes
TILE_SIZE = 32
SCREEN_WIDTH = 20 * TILE_SIZE
SCREEN_HEIGHT = 15 * TILE_SIZE

# Couleurs
COLOR_BG = (50, 50, 50)
COLOR_WALL = (100, 100, 100)
COLOR_GRASS = (50, 200, 50)
COLOR_PLAYER = (200, 50, 50)

# Charger le niveau
with open("level.json", "r") as f:
    level = json.load(f)

def get_colliding_tiles():
    collisions = []
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == 1:  # Mur
                tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                collisions.append(tile_rect)
    return collisions

player = Player(32, 32, 28, 28, COLOR_PLAYER, 4, get_colliding_tiles())
gun = Gun(player, 30)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = player.handle_input(keys)
    player.move(dx, dy)
    player.update_angle_to_mouse()
    player.rotate(player.angle)
    
    gun.update()

    # Affichage
    screen.fill(COLOR_BG)
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == 1:
                pygame.draw.rect(screen, COLOR_WALL, rect)
            elif tile == 2:
                pygame.draw.rect(screen, COLOR_GRASS, rect)
                
    player.draw(screen)
    gun.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()