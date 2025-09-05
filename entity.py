import pygame

class Entity:
    def __init__(self, x, y, width, height, color, colliding_tiles=[]):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.colliding_tiles = colliding_tiles
        self.angle = 0

    def draw(self, surface):
        # Dessin avec rotation
        image = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(image, self.color, image.get_rect())
        rotated_image = pygame.transform.rotate(image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect.topleft)

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
                    
    def rotate(self, angle):
        self.angle = angle
