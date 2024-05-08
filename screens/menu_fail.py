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

class Menu_Fail:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.title_text = self.title_font.render("SPACIN", True, WHITE)
        self.fail_message_text = self.font.render("Puts, você foi atingido! Tente novamente e pegue mais estrelas dessa vez.", True, WHITE)
        self.continue_text = self.font.render("CONTINUE", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.fail_message_rect = self.fail_message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.continue_rect = self.continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))
        self.should_start_game = False

    def draw(self, surface):
        surface.fill(BLUE)
        surface.blit(self.title_text, self.title_rect)
        surface.blit(self.fail_message_text, self.fail_message_rect)
        pygame.draw.rect(surface, WHITE, self.continue_rect, 2)
        surface.blit(self.continue_text, self.continue_rect)

    def update(self):
        self.should_start_game = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.continue_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.should_start_game = True

        return False
