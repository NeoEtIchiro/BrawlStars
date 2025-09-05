import pygame
import math

from entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height, color, speed, colliding_tiles=[]):
        super().__init__(x, y, width, height, color, colliding_tiles)
        self.speed = speed
        self.angle = 0

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
        return dx, dy

    def update_angle_to_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_center = self.rect.center
        dx = mouse_x - player_center[0]
        dy = mouse_y - player_center[1]
        self.angle = math.degrees(math.atan2(-dy, dx))  # -dy car pygame y va vers le bas