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

    def handle_events(self, event):
        print("handle event game")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update_game(self):
        current_time = pygame.time.get_ticks()
        self.all_sprites.add(self.player)
        if len(self.meteors) < self.MAX_METEORS and current_time - self.meteor_spawn_timer > 1500:
            meteor = Meteor()
            self.all_sprites.add(meteor)
            self.meteors.add(meteor)
            self.meteor_spawn_timer = current_time

        self.all_sprites.update()

        if pygame.sprite.spritecollide(self.player, self.meteors, False):
            self.running = False

        star_collected = pygame.sprite.spritecollide(self.player, self.stars, True)
        for star in star_collected:
            self.player.collect_star(star)

        if current_time - self.star_spawn_timer > 1800:
            star = Star()
            self.all_sprites.add(star)
            self.stars.add(star)
            self.star_spawn_timer = current_time

    def draw(self, screen):
        print("draw game")

        screen.fill((0, 0, 0))

        self.all_sprites.draw(screen)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Pontuação: {self.player.score}", True, (255, 255, 255))
        self.screen.blit(text_surface, (20, 20))

        if self.player.show_notification:
            notification_font = pygame.font.Font(None, 24)
            notification_text_surface = notification_font.render("New card unlocked!", True, (255, 255, 255))
            self.screen.blit(notification_text_surface, (400, 50))

        pygame.display.flip()

    def is_done(self):
        return not self.running

    # def start_game(self, player):
    #     self.player = player
    #     self.all_sprites.add(player)

    # def set_user_data(self, dados_usuarios):
    #     self.dados_usuarios = dados_usuarios
