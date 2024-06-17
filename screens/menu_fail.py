import pygame

from assets.alien import Alien
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
        self.fail_message_text = self.font.render("Puts, você foi atingido :( Pegue mais estrelas!", True, WHITE)
        self.continue_text = self.font.render("TRY AGAIN", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.fail_message_rect = self.fail_message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.continue_rect = self.continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))
        self.should_start_game = False

        # Carregar imagem de fundo
        self.background_image = pygame.image.load('login.jpg').convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Criar o alienígena
        self.alien = Alien('alien.png', SCREEN_WIDTH - 70, 50)

    def draw(self, surface):
        # Desenhar imagem de fundo
        surface.blit(self.background_image, (0, 0))

        # Desenhar alienígena
        self.alien.draw(surface)

        # Desenhar texto e botões
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

