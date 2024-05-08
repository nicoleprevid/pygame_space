import pygame
import random

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

# Classe para representar a tela inicial (menu)
class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 72)
        self.continue_text = self.font.render("CONTINUE", True, WHITE)
        self.title_text = self.title_font.render("SPACIN", True, WHITE)
        self.continue_rect = self.continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.should_start_game = False

    def draw(self, surface):
        surface.fill(BLACK)
        surface.blit(self.title_text, self.title_rect)
        pygame.draw.rect(surface, WHITE, self.continue_rect, 2)
        surface.blit(self.continue_text, self.continue_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.continue_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.should_start_game = True

        return False
