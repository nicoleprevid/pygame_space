import pygame
import json
from screens.login import LoginScreen
from screens.menu import Menu
from screens.menu_fail import Menu_Fail
from screens.menu_sucess import Menu_Success
from screens.game import GameScreen
from screens.pause_menu import PauseMenu
from screens.quiz import QuizGame
from screens.menu_cards import Menu_Cards



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
quiz = QuizGame(screen)
login_screen = LoginScreen()

# Inicialização do menu
menu_screen = Menu()
menu_fail = Menu_Fail()
menu_sucess = Menu_Success()
pause_menu = PauseMenu(screen)
# Loop principal do jogo
current_screen = "login"
running = True
player_new = False
clock = pygame.time.Clock()
new_quiz = False
menu_card = Menu_Cards()
background_music = pygame.mixer.Sound('background1.mp3')
pygame.display.set_caption('Spacin')
background_music.play(loops=-1) 
            
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_screen == "login":
            login_screen.handle_events(event)

    if current_screen == "login":

        login_screen.draw(screen)
        if login_screen.is_done:
            player = login_screen.validar_login(login_screen.input_text)
            game_screen = GameScreen(screen, player)
            print (player)
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
        pygame.mixer.unpause()
        game_screen.paused = False
        if (player_new == True):
            login_screen2 = LoginScreen()
            
            # REINICIA ATRIBUTOS
            
            player = login_screen2.validar_login(login_screen.player.username)
            print ("valor de player.username no menu fail  : " + login_screen.player.username ) 
            
            game_screen = GameScreen(screen, player)
            game_screen.handle_events(event)
            game_screen.update_game()
            game_screen.draw(screen)
            
            if game_screen.is_done():
                current_screen = "menu_fail"
            if game_screen.success:
                current_screen = "menu_sucess"
            if game_screen.handle_pause_menu_events(event) == True:
                current_screen = "pause_menu"
            player_new = False
        else:
    
            game_screen.handle_events(event)
            game_screen.update_game()
            game_screen.draw(screen)
            if game_screen.is_done():
                current_screen = "menu_fail"
            if game_screen.success:
                current_screen = "menu_sucess"
            if game_screen.handle_pause_menu_events(event) == True:
                current_screen = "pause_menu"

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
            if (nivel >= 9 ):
                current_screen = "menu_card"
            else:
                player_new = True
                current_screen = "game" 
                print("abre game")
                
    elif current_screen == "menu_card":
        menu_card.update()
        menu_card.draw(screen)
        if menu_card.quiz():
            current_screen = "quiz"
            

            
    elif current_screen == "pause_menu":
        
        pause_menu.handle_events()
        pause_menu.draw()
        if pause_menu.paused == False:
            current_screen = "game"
            
    elif current_screen == "quiz":
        if new_quiz == True:
            quiz2 = QuizGame(screen)
            print ("quiz new")
            quiz2.run()
            if quiz2.is_try_again() == True:
                current_screen = "quiz"
                new_quiz = True
                quiz.running = False
            if quiz2.is_go_to_menu() == True:
                pygame.quit
        else:
            print ("quiz")
            quiz.run()
            if quiz.is_try_again():
                current_screen = "quiz"
                new_quiz = True
                quiz = QuizGame(screen)
                quiz.running = False
            if quiz.is_go_to_menu():
                print ("is_go_to_menu() funcincou ")
                pygame.quit
            
        
            
    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Limita a taxa de quadros

pygame.quit()
