import pygame
import math

class Bullet:
    def __init__(self, x, y, angle, speed=10, colliding_tiles=[], enemies=[]):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = 5
        self.colliding_tiles = colliding_tiles
        self.enemies = enemies
        self.color = (255, 0, 0)
        self.active = True 

    def update(self):
        if not self.active:
            return
        
        rad_angle = math.radians(self.angle)
        self.x += self.speed * math.cos(rad_angle)
        self.y -= self.speed * math.sin(rad_angle) 
        
        bullet_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        for tile in self.colliding_tiles:
            if bullet_rect.colliderect(tile):
                self.active = False

        # Vérifie seulement les ennemis actifs
        for enemy in [e for e in self.enemies if getattr(e, "active", True)]:
            if bullet_rect.colliderect(enemy.rect):
                enemy.change_health(-20)
                self.active = False

    def draw(self, surface):
        if self.active:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)