import pygame
import random

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 20
        self.image = pygame.image.load("assets\\star.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))  # Redimensiona para o tamanho do triângulo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.uniform(1, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.uniform(1, 4)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
