import pygame
import random

WIDTH = 500
HEIGHT = 800

FPS = 60
GRAVITY = 0.4

PLATFORM_GAP = 120
MAX_PLATFORMS = 15

BG_IMG = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT))

DOODLE_IMG_RIGHT = pygame.transform.scale(pygame.image.load("images/doodle.png"), (50, 50))

DOODLE_IMG_LEFT = pygame.transform.flip(DOODLE_IMG_RIGHT, True, False), (50, 50)

DOODLE_FLY_IMG_RIGHT = pygame.transform.scale(pygame.image.load("images/doodle_fly.png"), (50, 50))

DOODLE_FLY_IMG_LEFT = pygame.transform.flip(DOODLE_FLY_IMG_RIGHT, True, False), (50, 50)

SPRING_IMG = pygame.transform.scale(pygame.image.load("images/spring.png"), (50, 50))

JETPACK_IMG = pygame.transform.scale(pygame.image.load("images/jetpack.png"), (50, 50))

