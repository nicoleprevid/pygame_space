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

# # Classe para representar as estrelas (triângulos)
# class Star(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.size = 20
#         self.color = BLUE
#         self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - self.size),
#                                  random.randint(-100, -40), self.size, self.size)
#         self.speed_y = random.uniform(0.5, 1.5)  # Velocidade aleatória mais lenta

#     def update(self):
#         self.rect.y += self.speed_y
#         if self.rect.top > SCREEN_HEIGHT:
#             self.rect.x = random.randint(0, SCREEN_WIDTH - self.size)
#             self.rect.y = random.randint(-100, -40)
#             self.speed_y = random.uniform(0.5, 1.5)  # Regenera com nova velocidade aleatória

#     def draw(self, surface):
#         pygame.draw.polygon(surface, self.color,
#                             [(self.rect.centerx, self.rect.top),
#                              (self.rect.left, self.rect.bottom),
#                              (self.rect.right, self.rect.bottom)])

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 20
        self.image = pygame.image.load("spacin\\assets\\star.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))  # Redimensiona para o tamanho do triângulo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.uniform(0.5, 1.5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.uniform(0.5, 1.5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
