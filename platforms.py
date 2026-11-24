from settings import *

class Platform:
    WIDTH = 100
    HEIGHT = 30

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.color = (0, 200, 0)
        self.vel_y = 0

    def update(self):
        pass

    def draw(self, screen, camera_y):
        pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, self.WIDTH, self.HEIGHT), border_radius = 18)
    def on_land(self, doodle):
        doodle.jump()

class MovingPlatform(Platform):
    def __init__(self, x, y, move_range = 100, speed = 2):
        super().__init__(x, y)
        self.color = (0, 150, 255)
        self.start_x = x
        self.move_range = move_range
        self.speed = speed
        self.direction = 1
    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x > self.start_x + self.move_range:
            self.rect.x = self.start_x + self.move_range
            self.direction *= -1
        elif self.rect.x < self.start_x - self.move_range:
            self.rect.x = self.start_x - self.move_range
            self.direction *= -1

class FallingPlatform(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (200, 200, 0)
        self.triggered = False
    def update(self):
        if self.triggered:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
        def on_land(self, doodle):
            super.on_land(doodle)
            self.triggered = True