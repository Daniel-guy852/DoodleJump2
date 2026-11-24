from platforms import Platform, FallingPlatform, MovingPlatform
from boosts import *

class InputHandler:
    def update(self, doodle):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            doodle.move(-1)
        if keys[pygame.K_d]:
            doodle.move(1)

class Camera:
    def __init__(self):
        self.y = 0
    def update(self, doodle):
        trigger = HEIGHT // 2
        if doodle.rect.y < self.y + trigger:
            delta = (self.y + trigger) - doodle.rect.y
            self.y -= delta
        score = - self.y // 10
        return score


class PlatformSpawner:
    def spawn(self, platforms, boosts):
        highest = min(p.rect.y for p in platforms)
        while len(platforms) < MAX_PLATFORMS:
            x = random.randint(50, WIDTH - 150)
            y = highest - PLATFORM_GAP
            platforms.append(Platform(x, y))
            PlatformClass = random.choices([Platform, FallingPlatform, MovingPlatform], weights=[0.5, 0.25, 0.25])[0]
            platform = PlatformClass(x, y)
            platforms.append(platform)

            if random.random() < 0.2:
                boosts.append(BoostType(platform))
            highest = y

class CollisionManager:
    def handler(self, doodle, platforms, boosts):
        for platform in platforms:
            if doodle.rect.colliderect(platform.rect) and doodle.vel_y > 0:
                platform.on_land(doodle)
            platform.update()
        for boost in boosts[:]:
            if doodle.rect.colliderect(boost.rect):
                boost.apply(doodle)
                boosts.remove(boost)

class UI:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 30)
        self.big_font = pygame.font.SysFont(None, 40)
    def draw(self, screen, score, game_over):
        score_text = self.font.render(f"Height: {int(score)}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            screen.blit(overlay, (0, 0))
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            texts = [self.big_font.render("GAME OVER", True, (255, 255, 255)),
            self.font.render(f"final height: {int(score)}", True, (255, 255, 255)),
            self.font.render("press R to restart", True, (255, 255, 255))]

            y = HEIGHT // 2 - 80
            for text in texts:
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y))
                y += 50