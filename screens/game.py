
import pygame
from assets.star import Star
from assets.meteor import Meteor
class GameScreen:
    def __init__(self, screen, player):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.running = True
        self.meteor_spawn_timer = 0
        self.star_spawn_timer = 0
        self.MAX_METEORS = 5
        self.current_card_index = 0
        self.success = False
        self.nivel = self.player.level_actived 
        # Cores para o botão de pausa
        self.pause_button_color = (100, 100, 100)
        self.pause_button_rect = pygame.Rect(700, 20, 70, 30)
        
        # Carregar sons
        self.star_sound = pygame.mixer.Sound('star.mp3')
        self.meteor_sound = pygame.mixer.Sound('die.mp3')
 
        # Carregar imagens de fundo para cada nível
        self.backgrounds = [
            pygame.image.load('1.jpg').convert(),
            pygame.image.load('2.jpg').convert(),
            pygame.image.load('3.jpg').convert(),
            pygame.image.load('4.jpg').convert(),
            pygame.image.load('5.jpg').convert(),
            pygame.image.load('6.jpg').convert(),
            pygame.image.load('7.jpg').convert(),
            pygame.image.load('8.jpg').convert(),
            
        ]
        
        # Redimensiona as imagens de fundo para preencher toda a tela
        self.backgrounds = [pygame.transform.scale(background, (screen.get_width(), screen.get_height() * 1.5 )) for background in self.backgrounds]


        # Estado do jogos
        self.paused = False

    def handle_events(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
        # self.handle_pause_menu_events(event)  # Chama o método para tratar os eventos do menu de pausa

    def update_game(self):
        if not self.paused:
            current_time = pygame.time.get_ticks()
            self.all_sprites.add(self.player)
            self.MAX_METEORS = self.MAX_METEORS + self.nivel
            meteor_speed = 1 + self.nivel / 9 # Aumenta a velocidade dos meteoros
            if len(self.meteors) < self.MAX_METEORS and current_time - self.meteor_spawn_timer > 1500 / (self.nivel * 0.5):
                meteor = Meteor(speed=meteor_speed)  # Passa a velocidade como parâmetro
                self.all_sprites.add(meteor)
                self.meteors.add(meteor)
                self.meteor_spawn_timer = current_time

            self.all_sprites.update()

            # Verifica colisões com estrelas
            star_collected = pygame.sprite.spritecollide(self.player, self.stars, True)
            for star in star_collected:
                self.player.collect_star(star)
                self.star_sound.play()  # Reproduz o som de colisão com estrelas

            # Verifica colisões com meteoros
            if pygame.sprite.spritecollide(self.player, self.meteors, False):
                self.running = False
                self.meteor_sound.play() 
                pygame.mixer.pause()

                 # Reproduz o som de colisão com meteoros

            # Spawna estrelas
            if current_time - self.star_spawn_timer > 500 / (self.nivel * 0.5):
                star = Star()
                self.all_sprites.add(star)
                self.stars.add(star)
                self.star_spawn_timer = current_time

            # Aumenta o nível do jogador
            if self.player.score >= 10:
                self.success = True
                self.player.level_actived += 1
                self.player.unlock_card()
                self.star_sound.play()
                pygame.mixer.pause()

                
    def draw(self, screen):
        if(self.player.level_actived < 9):
            self.screen.blit(self.backgrounds[self.player.level_actived - 1], (0, -140))

            font = pygame.font.Font(None, 36)
            text_surface = font.render(f"Pontuação: {self.player.score}", True, (255, 255, 255))
            text_nivel = font.render(f"Nivel: {self.nivel}", True, (255, 255, 255))

            self.screen.blit(text_surface, (20, 20))
            self.screen.blit(text_nivel, (40, 40))

            if self.player.show_notification:
                notification_font = pygame.font.Font(None, 24)
                notification_text_surface = notification_font.render("New card unlocked!", True, (255, 255, 255))
                self.screen.blit(notification_text_surface, (400, 50))

            # Desenha o botão de pausa
            pygame.draw.rect(screen, self.pause_button_color, self.pause_button_rect)
            font = pygame.font.Font(None, 24)
            text_surface = font.render("Pause", True, (255, 255, 255))
            screen.blit(text_surface, (710, 25))

            # Desenha os sprites
            self.all_sprites.draw(self.screen)
            
            pygame.display.flip()
        
    def handle_pause_menu_events(self, event):
        self.paused = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.pause_button_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.paused = True 
                print ("pause")
                
        return self.paused 
                
    def is_paused (self):
        return self.paused 
    
    def is_done(self):
        return not self.running
