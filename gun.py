import pygame
import math

class Gun:
    def __init__(self, owner, offset_x):
        self.owner = owner
        self.offset_x = offset_x
        self.angle = 0

    def update(self):
        # Place le gun devant le joueur selon l'angle
        rad_angle = math.radians(self.owner.angle)
        self.x = self.owner.rect.centerx + self.offset_x * math.cos(rad_angle)
        self.y = self.owner.rect.centery - self.offset_x * math.sin(rad_angle)
        self.angle = self.owner.angle  # Synchronise l'angle du gun avec le joueur

    def draw(self, surface):
        width, height = 20, 8  # dimensions du rectangle
        gun_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(gun_surface, (0, 0, 0), (0, 0, width, height))
        rotated_gun = pygame.transform.rotate(gun_surface, self.angle)
        rotated_rect = rotated_gun.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated_gun, rotated_rect.topleft)