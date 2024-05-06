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
# GREEN = (0, 255, 0)

# # Classe para representar a nave espacial (jogador)
# class Player(pygame.sprite.Sprite):
#     def __init__(self, username, cards_unlocked):
#         super().__init__()
#         self.username = username
#         self.cards_unlocked = cards_unlocked
#         self.width = 30
#         self.height = 50
#         self.color = WHITE
#         self.rect = pygame.Rect(SCREEN_WIDTH // 2 - self.width // 2, SCREEN_HEIGHT // 2 - self.height // 2, self.width, self.height)
#         self.speed = 8
#         self.score = 0
#         self.vertical_speed = 0  # Velocidade vertical de subida (agora zero)
#         self.notification_timer = 0
#         self.show_notification = False
#         self.cards = []

#     def update(self):
#         # Mantém o jogador parado no centro vertical da tela
#         self.rect.y += self.vertical_speed

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] and self.rect.left > 0:
#             self.rect.x -= self.speed
#         if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
#             self.rect.x += self.speed

#         # Verifica se a pontuação é um múltiplo de 10
#         if self.score > 0 and self.score % 10 == 0:
#             self.show_notification = True
#             self.notification_timer = pygame.time.get_ticks()  # Reinicia o timer

#         # Atualiza o timer da notificação
#         if self.show_notification and pygame.time.get_ticks() - self.notification_timer > 1500:
#             self.show_notification = False  # Oculta a notificação após 1.5 segundos

#     def draw(self, surface):
#         pygame.draw.rect(surface, self.color, self.rect)

#     def collect_star(self, star):
#         self.score += 1
#         star.kill()  # Remove a estrela da tela quando coletada

#     def unlock_card(self):
#         if self.score > 0 and self.score % 10 == 0 and self.score // 10 <= len(self.cards):
#             card = self.cards[self.score // 10 - 1]
#             if not card.unlocked:
#                 card.unlocked = True
#                 return card.name
#         return None

class Player(pygame.sprite.Sprite):
    def __init__(self, username, cards_unlocked):
        super().__init__()
        self.username = username
        self.cards_unlocked = cards_unlocked
        self.width = 30
        self.height = 50

        # Carrega a imagem PNG e redimensiona para o tamanho do retângulo
        self.image = pygame.image.load("spacin\\assets\\rocket.webp")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Ajusta o retângulo para as dimensões da imagem
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.speed = 8
        self.score = 0
        self.vertical_speed = 0  
        self.notification_timer = 0
        self.show_notification = False
        self.cards = []

    def update(self):
        # Mantém o jogador parado no centro vertical da tela
        self.rect.y += self.vertical_speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

        if self.score > 0 and self.score % 10 == 0:
            self.show_notification = True
            self.notification_timer = pygame.time.get_ticks()  

        if self.show_notification and pygame.time.get_ticks() - self.notification_timer > 1500:
            self.show_notification = False  

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collect_star(self, star):
        self.score += 1
        star.kill()  

    def unlock_card(self):
        if self.score > 0 and self.score % 10 == 0 and self.score // 10 <= len(self.cards):
            card = self.cards[self.score // 10 - 1]
            if not card.unlocked:
                card.unlocked = True
                return card.name
        return None
