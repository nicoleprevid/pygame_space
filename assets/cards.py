import pygame

class Card:
    def __init__(self, name, unlocked=False):
        self.name = name
        self.unlocked = unlocked
        self.width = 60  # largura em pixels
        self.height = 40  # altura em pixels
        self.border_radius = 5  # raio do canto arredondado
        self.text_color = (255, 255, 255)  # cor do texto (branco)
        self.background_color = (72, 27, 128)  # cor de fundo (roxo escuro)
        self.shadow_color = (0, 0, 0)  # cor da sombra (preto)
        self.shadow_offset = 2  # deslocamento da sombra em pixels

    def draw(self, screen, x, y):
        # Desenhar o retângulo da carta
        pygame.draw.rect(screen, self.shadow_color, (x + self.shadow_offset, y + self.shadow_offset, self.width, self.height))
        pygame.draw.rect(screen, self.background_color, (x, y, self.width, self.height), border_radius=self.border_radius)

        # Adicionar texto à carta
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(self.name, True, self.text_color)
        text_rect = text_surface.get_rect(center=(x + self.width // 2, y + self.height // 2))
        screen.blit(text_surface, text_rect)
