import pygame
import math
import random as Random

from entity import Entity

class Enemy(Entity):
    def __init__(self, pos, width, height, color, speed, colliding_tiles=[], hidding_tiles=[]):
        super().__init__(pos, width, height, color, colliding_tiles, hidding_tiles)
        self.speed = speed
        self.angle = 0
        self.direction_timer = 0
        self.direction_interval = 90
        self.dx = 0
        self.dy = 0
        self.state = "moving"

    def update(self):
        super().update()
        dx, dy = self.handle_input()
        self.move(dx, dy)

        if self.state == "moving":
            self.rotate(self.update_angle_to_move())

    def handle_input(self):
        self.direction_timer += 1
        if self.direction_timer >= self.direction_interval:
            self.dx = Random.choice([-self.speed, 0, self.speed])
            self.dy = Random.choice([-self.speed, 0, self.speed])
            self.direction_timer = 0

        if self.dx != 0 or self.dy != 0:
            length = math.hypot(self.dx, self.dy)
            self.dx = self.dx / length * self.speed
            self.dy = self.dy / length * self.speed

        return self.dx, self.dy

    def update_angle_to_move(self):
        if self.dx == 0 and self.dy == 0:
            return self.angle 
        return math.degrees(math.atan2(-self.dy, self.dx)) 