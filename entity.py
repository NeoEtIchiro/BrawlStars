import pygame

from gun import Gun

class Entity:
    def __init__(self, pos, width, height, color, colliding_tiles=[], hidding_tiles=[], enemies=[]):
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.color = color
        self.colliding_tiles = colliding_tiles
        self.hidding_tiles = hidding_tiles
        self.angle = 0
        self.health = 100
        self.enemies = enemies
        self.gun = None
        self.active = True
        self.hidden = False

    def update(self):
        self.gun.update()

    def draw(self, surface):
        # Désature légèrement la couleur si hidden
        if self.hidden:
            r, g, b = self.color
            gray = int(0.3 * r + 0.59 * g + 0.11 * b)
            # Mélange couleur originale et gris (50% chacun)
            color = (
                int(r * 0.7 + gray * 0.3),
                int(g * 0.7 + gray * 0.3),
                int(b * 0.7 + gray * 0.3)
            )
        else:
            color = self.color

        image = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(image, color, image.get_rect())
        rotated_image = pygame.transform.rotate(image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect.topleft)
        
        self.gun.draw(surface)

    def move(self, dx, dy):
        # Mouvement sur X
        self.rect.x += dx
        for collidable in self.colliding_tiles:
            if self.rect.colliderect(collidable):
                if dx > 0:
                    self.rect.right = collidable.left
                elif dx < 0:
                    self.rect.left = collidable.right
        # Mouvement sur Y
        self.rect.y += dy
        for collidable in self.colliding_tiles:
            if self.rect.colliderect(collidable):
                if dy > 0:
                    self.rect.bottom = collidable.top
                elif dy < 0:
                    self.rect.top = collidable.bottom

        # Détection des hidding tiles
        self.hidden = False
        for hidding_tile in self.hidding_tiles:
            if self.rect.colliderect(hidding_tile):
                self.hidden = True
                break
                    
    def rotate(self, angle):
        self.angle = angle
        
    def change_health(self, amount):
        self.health += amount
        self.health = max(0, min(100, self.health))
        
        if(self.health <= 0):
            self.active = False
        
    def set_enemies(self, enemies):
        self.enemies = enemies
        self.gun = Gun(self, 30, self.colliding_tiles)
