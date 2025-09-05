import pygame
import json
import random as Random

from player import Player
from enemy import Enemy

# Constantes
TILE_SIZE = 32
SCREEN_WIDTH = 20 * TILE_SIZE
SCREEN_HEIGHT = 15 * TILE_SIZE

# Entity consts
SPEED = 1.5

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

def get_hidding_tiles():
    hiddings = []
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == 2:  # Herbe
                tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                hiddings.append(tile_rect)
    return hiddings

def get_valid_spawn_positions():
    positions = []
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == 0:
                positions.append((x * TILE_SIZE + TILE_SIZE//2, y * TILE_SIZE + TILE_SIZE//2))
    return positions[Random.randint(0, len(positions)-1)]

colliding_tiles = get_colliding_tiles()
hidding_tiles = get_hidding_tiles()

player = Player((32, 32), 28, 28, COLOR_PLAYER, SPEED, colliding_tiles, hidding_tiles)
enemies = [Enemy(get_valid_spawn_positions(), 28, 28, (200, 200, 50), SPEED, colliding_tiles, hidding_tiles) for _ in range(5)]

player.set_enemies(enemies)
for enemy in enemies:
    enemy.set_enemies([e for e in enemies if e != enemy] + [player])

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.gun.shoot()

    player.update()
    
    for enemy in enemies:
        enemy.update()
    
    if(not player.active):
        print("Game Over")
        running = False
        
    enemies = [e for e in enemies if e.active]
    if(len(enemies) == 0):
        print("You Win!")
        running = False

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

    if player.hidden:
        for enemy in enemies:
            enemy.draw(screen)
    else:
        for enemy in [e for e in enemies if not e.hidden]:
            enemy.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()