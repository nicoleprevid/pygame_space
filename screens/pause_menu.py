import pygame 
class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.return_button_rect = pygame.Rect(250, 200, 300, 50)
        self.quit_button_rect = pygame.Rect(250, 270, 300, 50)
        self.sound_button_rect = pygame.Rect(250, 340, 300, 50)
        self.button_color = (100, 100, 100)
        self.active_color = (200, 200, 200)
        self.paused = True
        self.sound_on = True
        self.sound_button_clicked = False  # Variável para controlar se o botão de som foi clicado

    def handle_events(self):
        self.paused = True
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.return_button_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.toggle_pause()  # Retorna ao jogo
        elif self.quit_button_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                pygame.quit()  # Sai do jogo
        elif self.sound_button_rect.collidepoint(mouse_pos):
            if mouse_clicked and not self.sound_button_clicked:  # Verifica se o botão ainda não foi clicado
                self.toggle_sound()  # Alterna o som ligado/desligado
                self.sound_button_clicked = True  # Atualiza a variável para indicar que o botão foi clicado
        else:
            self.sound_button_clicked = False  # Redefine a variável se nenhum botão estiver sendo clicado

    def draw(self):
        if self.paused:
            # Desenha o fundo do menu
            pygame.draw.rect(self.screen, (50, 50, 50), (200, 150, 400, 300))
            
            # Desenha os botões
            pygame.draw.rect(self.screen, self.button_color, self.return_button_rect)
            pygame.draw.rect(self.screen, self.button_color, self.quit_button_rect)
            pygame.draw.rect(self.screen, self.button_color, self.sound_button_rect)

            # Desenha o texto nos botões
            return_text = self.font.render("Return to game", True, (255, 255, 255))
            quit_text = self.font.render("Quit", True, (255, 255, 255))
            sound_text = self.font.render("Sound: " + ("ON" if self.sound_on else "OFF"), True, (255, 255, 255))
            self.screen.blit(return_text, (270, 210))
            self.screen.blit(quit_text, (330, 280))
            self.screen.blit(sound_text, (280, 350))

    def toggle_pause(self):
        self.paused = not self.paused

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        if not self.sound_on:
            pygame.mixer.pause()  # Pausa todos os sons
            self.sound_on = False
            print("pause")
        else:
            pygame.mixer.unpause()  # Retoma a reprodução dos sons
            print("unpause")
            self.sound_on = True
