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
        self.continue_text = self.font.render("START GAME", True, WHITE)
        self.title_text = self.title_font.render("SPACIN", True, WHITE)
        self.welcome_text = self.font.render("Bem-vindo ao jogo que te leva ao espaço!", True, WHITE)
        
        # Define a posição e as dimensões do retângulo em volta do botão "CONTINUE"
        self.continue_rect = pygame.Rect((SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 130 , 300, 50))  # Aumenta a largura do retângulo
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 190))
        self.welcome_rect = self.welcome_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 130))  # Posiciona a frase de boas-vindas abaixo do título
        self.should_start_game = False

        # Carregar imagem de fundo para o menu
        self.background = pygame.image.load('fundo_menu.webp').convert()

        new_width = int(self.background.get_width() * 1.2)
        new_height = int(self.background.get_height() * 1.2)
        self.background = pygame.transform.scale(self.background, (new_width, new_height))

    def draw(self, surface):
        # Desenha a imagem de fundo
        surface.blit(self.background, (0, 0))

        # Desenha o título, a frase de boas-vindas e o botão "CONTINUE"
        surface.blit(self.title_text, self.title_rect)
        surface.blit(self.welcome_text, self.welcome_rect)  
        pygame.draw.rect(surface, WHITE, self.continue_rect, 2)
        # Centraliza o texto "CONTINUE" dentro do retângulo
        continue_text_rect = self.continue_text.get_rect(center=self.continue_rect.center)
        surface.blit(self.continue_text, continue_text_rect.topleft)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.continue_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.should_start_game = True

        return False
