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

class Meteor(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.radius = random.randint(15, 40)
        self.image = pygame.image.load("assets\\meteor.png")
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))  # Redimensiona para o dobro do raio
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.uniform( speed, speed+2)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.uniform(self.speed_y, self.speed_y +2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
