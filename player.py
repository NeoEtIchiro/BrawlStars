import pygame
import math

from entity import Entity

class Player(Entity):
    def __init__(self, pos, width, height, color, speed, colliding_tiles=[], hidding_tiles=[]):
        super().__init__(pos, width, height, color, colliding_tiles, hidding_tiles)
        self.speed = speed

    def update(self):
        super().update()
        dx, dy = self.handle_input(pygame.key.get_pressed())
        self.move(dx, dy)
        
        self.rotate(self.update_angle_to_mouse())

    def handle_input(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed
            
        if dx != 0 or dy != 0:
            length = math.hypot(dx, dy)
            dx = dx / length * self.speed
            dy = dy / length * self.speed

        return dx, dy

    def update_angle_to_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_center = self.rect.center
        dx = mouse_x - player_center[0]
        dy = mouse_y - player_center[1]
        return math.degrees(math.atan2(-dy, dx))