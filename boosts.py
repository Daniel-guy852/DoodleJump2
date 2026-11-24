from settings import *
from enum import Enum

class BoostType(Enum):
    SPRING = 1
    JETPACK = 2

    def __init__(self, platform):
        self.rect = pygame.Rect(platform.rect.centerx - 25, platform.rect.centery - 50, 50, 50)
        if random.random() < 0.2:
            self.type = BoostType.JETPACK
            self.image = JETPACK_IMG
        else:
            self.type = BoostType.SPRING
            self.image = SPRING_IMG
    def apply(self, doodle):
        if self.type == BoostType.SPRING:
            doodle.jump(-30)
        elif self.type == BoostType.JETPACK:
            doodle.image = doodle.fly_image
            doodle.jump(-80)
            doodle.flying = True
    def draw(self, screen, camera_y):
        screen.blit(self.image, (self.rect.x, self.rect.y - camera_y))