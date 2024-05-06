import pygame
import json
from screens.login import LoginScreen
from screens.menu import Menu
from screens.menu_fail import Menu_Fail

from screens.game import GameScreen

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SPACIN")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

dados_usuarios = []
# Carregar os dados dos usuários do arquivo JSON
try:
    with open("spacin\dados.json", "r") as file:
            dados_usuarios = json.load(file)
except FileNotFoundError:
    print("O arquivo 'spacin\dados.json' não foi encontrado.")

print (dados_usuarios)

# Inicialização da tela de login
login_screen = LoginScreen(dados_usuarios)

# Inicialização do menu
menu_screen = Menu()
menu_fail= Menu_Fail()

# Inicialização da tela do jogo
player = login_screen.validar_login(login_screen.input_text)
game_screen = GameScreen(screen, player)

# Loop principal do jogo
current_screen = "login"
running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_screen == "login":
            login_screen.handle_events(event)

    screen.fill(BLACK)  # Limpa a tela

    if current_screen == "login":
        login_screen.draw(screen)
        if login_screen.is_done:
            current_screen = "menu"   
            print("abre menu")


    elif current_screen == "menu":
        # menu_screen.handle_events(event)
        menu_screen.update()
        menu_screen.draw(screen)
        if menu_screen.should_start_game:
            current_screen = "game"
            print("abre game")

    elif current_screen == "game":
        game_screen.handle_events(event)
        game_screen.update_game()
        game_screen.draw(screen)
        if game_screen.is_done():
            current_screen = "menu_fail"

    elif current_screen == "menu_fail":
        menu_fail.update()
        menu_fail.draw(screen)
        if menu_fail.should_start_game:
            current_screen = "game"
            print("abre game")

    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Limita a taxa de quadros

pygame.quit()
