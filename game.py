import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Definição das configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Explorer")

# Carregamento de imagens
player_img = pygame.image.load('rocket.png').convert()
player_img.set_colorkey(BLACK)
meteor_img = pygame.image.load('meteoro.png').convert()
star_img = pygame.image.load('star.png').convert()
background_img = pygame.image.load('fundo.png').convert()
planet_imgs = [pygame.image.load('planet1.png').convert(), pygame.image.load('planet1.png').convert(), pygame.image.load('planet1.png').convert()]

# Relógio para controle de velocidade
clock = pygame.time.Clock()

# Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Classe dos meteoros
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = meteor_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)
            self.speed_x = random.randrange(-3, 3)

# Classe das estrelas
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = star_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# Classe dos planetas
class Planet(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed_y


# Classe do Quiz
class Quiz(pygame.sprite.Sprite):
    def __init__(self, question, options, correct_answer):
        super().__init__()
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

# Função para mostrar o texto na tela
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Função para mostrar o Quiz na tela
def show_quiz(quiz):
    screen.blit(background_img, (0, 0))
    draw_text(screen, quiz.question, 30, SCREEN_WIDTH // 2, 50, WHITE)

    option_y = 150
    for option in quiz.options:
        draw_text(screen, option, 24, SCREEN_WIDTH // 2, option_y, WHITE)
        option_y += 40

# Função para exibir a tela de fim de jogo
def show_end_screen(score):
    screen.blit(background_img, (0, 0))
    draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, WHITE)
    draw_text(screen, f"Score: {score}", 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
    draw_text(screen, "Pressione qualquer tecla para jogar novamente", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# Função principal do jogo
def main():
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    planets = pygame.sprite.Group()

    # Criação do jogador
    player = Player()
    all_sprites.add(player)

    # Criação dos meteoros
    for i in range(8):
        meteor = Meteor()
        all_sprites.add(meteor)
        meteors.add(meteor)

    # Criação das estrelas
    for i in range(10):
        star = Star()
        all_sprites.add(star)
        stars.add(star)

    # Criação dos planetas
    planet1 = Planet(planet_imgs[0])
    all_sprites.add(planet1)
    planets.add(planet1)

    # Variáveis do jogo
    score = 0
    running = True
    game_over = False

    # Loop do jogo
    while running:
        # Mantém o loop rodando na velocidade desejada
        clock.tick(60)

        # Processamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualização
        if not game_over:
            # Atualização das sprites
            all_sprites.update()

            # Verificação de colisão entre jogador e meteoros
            hits = pygame.sprite.spritecollide(player, meteors, False)
            if hits:
                game_over = True

            # Verificação de colisão entre jogador e estrelas
            star_hits = pygame.sprite.spritecollide(player, stars, True)
            for star in star_hits:
                score += 1

            # Verificação de colisão entre jogador e planetas
            planet_hits = pygame.sprite.spritecollide(player, planets, True)
            if planet_hits:
                # Mostrar o quiz
                quiz = Quiz("Qual é o planeta mais próximo do Sol?", ["Marte", "Vênus", "Mercúrio", "Terra"], "Mercúrio")
                show_quiz(quiz)
                pygame.display.flip()

                # Aguardar a resposta
                waiting = True
                while waiting:
                    clock.tick(30)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            waiting = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                answer = quiz.options[0]
                                waiting = False
                            elif event.key == pygame.K_2:
                                answer = quiz.options[1]
                                waiting = False
                            elif event.key == pygame.K_3:
                                answer = quiz.options[2]
                                waiting = False
                            elif event.key == pygame.K_4:
                                answer = quiz.options[3]
                                waiting = False

                # Verificar resposta
                if answer == quiz.correct_answer:
                    score += 10

        # Desenho / Renderização
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)
        draw_text(screen, f"Score: {score}", 24, SCREEN_WIDTH // 2, 10, WHITE)

        # Depois de desenhar tudo, vire a tela
        pygame.display.flip()

        # Tela de fim de jogo
        if game_over:
            show_end_screen(score)
            # Reinicie o jogo
            main()

    pygame.quit()

if __name__ == "__main__":
    main()
