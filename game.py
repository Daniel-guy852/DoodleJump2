from systems import *
from platforms import Platform
from doodle import Doodle


class World:
    def __init__(self):
        self.doodle = Doodle(255, 600)
        self.platforms = [Platform(200, 700)]
        self.boosts = []
        self.spawner = PlatformSpawner()
        self.collision_manager = CollisionManager()
        self.score = 0
        self.game_over = False

    def cleanup(self, camera):
        self.platforms = [p for p in self.platforms if p.rect.y - camera.y < HEIGHT]
        self.boosts = [u for u in self.boosts if u.rect.y - camera.y < HEIGHT]

    def update(self, camera):
        self.doodle.update()
        self.collision_manager.handle(self.doodle, self.platforms, self.boosts)
        self.score = max(self.score, camera.update(self.doodle))
        self.spawner.spawn(self.platforms, self.boosts)
        self.cleanup(camera)
        if self.doodle.rect.y - camera.y > HEIGHT:
            self.game_over = True
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.input = InputHandler()
        self.camera = Camera()
        self.ui = UI()
        self.reset()
    def reset(self):
        self.world = World()
        self.camera = Camera()
    def update(self):
        if self.world.game_over:
            return
        self.input.update(self.world.doodle)
        self.world.update(self.camera)
    def draw(self):
        bg_y = self.camera.y % HEIGHT
        self.screen.blit(BG_IMG, (0, -bg_y))
        self.screen.blit(BG_IMG, (0, HEIGHT - bg_y))

        for platform in self.world.platforms:
            platform.draw(self.screen, self.camera.y)
        for boost in self.world.boosts:
            boost.draw(self.screen, self.camera.y)
        self.world.doodle.draw(self.screen, self.camera.y)
        self.ui.draw(self.screen, self.world.score, self.world.game_over)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if self.world.game_over and pygame.key.get_pressed()[pygame.K_r]:
                self.reset()
            self.update()
            self.draaw()
            pygame.display.flip()
            self.clock.tick(FPS)