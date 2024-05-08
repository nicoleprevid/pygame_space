import pygame
import json
from screens.login import LoginScreen
from screens.menu import Menu
from screens.menu_fail import Menu_Fail
from screens.menu_sucess import Menu_Success
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

# Inicialização da tela de login
login_screen = LoginScreen()
player = login_screen.validar_login(login_screen.input_text)
game_screen = GameScreen(screen, player)
print (player)

# Inicialização do menu
menu_screen = Menu()
menu_fail = Menu_Fail()
menu_sucess = Menu_Success()

# Loop principal do jogo
current_screen = "login"
running = True
player_new = False
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
            player_new = False


    elif current_screen == "menu":
        # menu_screen.handle_events(event)
        menu_screen.update()
        menu_screen.draw(screen)
        if menu_screen.should_start_game:
            current_screen = "game"
            print("abre game")

    elif current_screen == "game":
        if (player_new == True):
            login_screen2 = LoginScreen()
            
            # REINICIA ATRIBUTOS
            player2 = login_screen2.validar_login(login_screen.player.username)
            print ("valor de player.username no menu fail  : " + login_screen.player.username ) 
            
            game_screen = GameScreen(screen, player2)
            game_screen.handle_events(event)
            game_screen.update_game()
            game_screen.draw(screen)
            
            if game_screen.is_done():
                current_screen = "menu_fail"
            if game_screen.success:
                current_screen = "menu_sucess"
            player_new = False
        else:
            game_screen.handle_events(event)
            game_screen.update_game()
            game_screen.draw(screen)
            if game_screen.is_done():
                current_screen = "menu_fail"
            if game_screen.success:
                current_screen = "menu_sucess"

    elif current_screen == "menu_fail":
        menu_fail.update()
        menu_fail.draw(screen)
        if menu_fail.should_start_game:
            # Reinicie os atributos do jogo
            player_new = True
            current_screen = "game" 
            print("abre game")
    
    elif current_screen == "menu_sucess":
        menu_sucess.update()
        menu_sucess.draw(screen)
        if menu_sucess.should_start_game:

            nivel = player.level_actived
            if (nivel >= 7):
                current_screen = "fim"
            else:
                player_new = True
                current_screen = "game" 
                print("abre game")


    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Limita a taxa de quadros

pygame.quit()
