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

class Menu_Success:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.title_text = self.title_font.render("SPACIN", True, WHITE)
        self.success_message_text = self.font.render("Parabéns! Novo card e planeta/nível desbloqueados!", True, WHITE)
        self.next_level_text = self.font.render("PRÓXIMO NÍVEL", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.success_message_rect = self.success_message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.next_level_rect = self.next_level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))
        self.should_start_game = False

    def draw(self, surface):
        surface.fill(YELLOW)
        surface.blit(self.title_text, self.title_rect)
        surface.blit(self.success_message_text, self.success_message_rect)
        pygame.draw.rect(surface, WHITE, self.next_level_rect, 2)
        surface.blit(self.next_level_text, self.next_level_rect)

    def update(self):
        self.should_start_game = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.next_level_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.should_start_game = True

        return False