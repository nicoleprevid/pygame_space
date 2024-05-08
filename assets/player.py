import pygame
import json

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

class Player(pygame.sprite.Sprite):
    def __init__(self, username, cards_unlocked, level):
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
        self.level_actived = level
        
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
        # Define a lista de nomes dos planetas
        planet_names = ["Mercurio", "Venus", "Terra", "Marte", "Jupiter", "Saturno", "Urano", "Netuno"]
        
        # Verifica se o nível ativo é maior do que o número de cards já desbloqueados
        if self.level_actived > len(self.cards_unlocked):
            # Adiciona o novo card ao final da lista de cards desbloqueados
            self.cards_unlocked.append(planet_names[self.level_actived - 2])  # -2 porque o nível 1 é o inicial
            
            # Atualiza o JSON do jogador com os cards desbloqueados
            self.update_player_json()
            
            # Retorna o nome do novo planeta desbloqueado
            return planet_names[self.level_actived - 2]
        else:
            return None

    def update_player_json(self):
        # Cria um dicionário para representar o jogador e seus dados
        player_data = {
            "username": self.username,
            "level": self.level_actived,
            "cards_unlocked": self.cards_unlocked
        }
        
        # Abre o arquivo JSON do jogador
        with open("spacin\\dados.json", "r+") as file:
            # Carrega os dados JSON existentes
            data = json.load(file)
            
            # Encontra o jogador no arquivo JSON e atualiza seus dados
            for player in data["players"]:
                if player["username"] == self.username:
                    player.update(player_data)
                    break
            
            # Move o cursor de arquivo para o início
            file.seek(0)
            
            # Escreve os dados JSON atualizados de volta para o arquivo
            json.dump(data, file)
            
            # Trunca o arquivo para o tamanho atual para remover dados antigos se necessário
            file.truncate()

        
        return None
