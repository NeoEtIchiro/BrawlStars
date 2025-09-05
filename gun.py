import pygame
import math

from bullet import Bullet

class Gun:
    def __init__(self, owner, offset_x, colliding_tiles=[]):
        self.owner = owner
        self.offset_x = offset_x
        self.angle = 0
        self.bullets = []
        self.colliding_tiles = colliding_tiles
        self.enemies = owner.enemies

    def update(self):
        # Place le gun devant le joueur selon l'angle
        rad_angle = math.radians(self.owner.angle)
        self.x = self.owner.rect.centerx + self.offset_x * math.cos(rad_angle)
        self.y = self.owner.rect.centery - self.offset_x * math.sin(rad_angle)
        self.angle = self.owner.angle  # Synchronise l'angle du gun avec le joueur
        
        for bullet in self.bullets:
            bullet.update()
        # Supprime les bullets inactives
        self.bullets = [b for b in self.bullets if b.active]

    def draw(self, surface):
        width, height = 20, 8  # dimensions du rectangle
        gun_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(gun_surface, (0, 0, 0), (0, 0, width, height))
        rotated_gun = pygame.transform.rotate(gun_surface, self.angle)
        rotated_rect = rotated_gun.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated_gun, rotated_rect.topleft)
        
        for bullet in self.bullets:
            bullet.draw(surface)
        
    def shoot(self):
        bullet = Bullet(self.x, self.y, self.angle, 10, self.colliding_tiles, self.enemies)
        self.bullets.append(bullet)