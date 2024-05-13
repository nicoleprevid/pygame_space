import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Alien:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load("alien.webp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))  # Redimensiona a imagem pela metade
        self.rect = self.image.get_rect()
        self.rect.topleft = self.calculate_position(x, y)

    def calculate_position(self, x, y):
        # Ajusta as coordenadas para garantir que o alienígena fique dentro da tela
        if x < 0:
            x = 0
        elif x > SCREEN_WIDTH - self.rect.width:
            x = SCREEN_WIDTH - self.rect.width
        if y < 0:
            y = 0
        elif y > SCREEN_HEIGHT - self.rect.height:
            y = SCREEN_HEIGHT - self.rect.height
        return (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
