from settings import *

class Doodle:
    def __init__(self, x, y):
        self.size = 50
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.image = DOODLE_IMG_RIGHT
        self.fly_image = DOODLE_FLY_IMG_RIGHT
        self.vel_y = 0
        self.jump_power = -15
        self.direction = 1
        self.on_ground = False
        self.flying = False
        self.speed_x = 5
    def jump(self, power = None):
        self.vel_y = power if power else self.jump_power

    def move(self, direction):
        self.direction = direction
        self.rect.x += direction * self.speed_x
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0
    def draw(self, screen, camera_y):
        screen.blit(self.image, (self.rect.x, self.rect.y - camera_y))

    def update(self):
        self.vel_y = min(self.vel_y + GRAVITY, 15)