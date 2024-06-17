import pygame
from assets.alien import Alien

class QuizGame:
    def __init__(self, screen):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = screen
        
        self.clock = pygame.time.Clock()
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 200, 0)
        self.RED = (200, 0, 0)
        self.questions = [
            {"question": "O Monte Olimpo, maior vulcão conhecido em todo o Sistema Solar, se encontra em qual planeta?",
             "options": [("a) Marte", "a"), ("b) Saturno", "b"), ("c) Netuno", "c"), ("d) Urano", "d")],
             "correct": "a"},

            {"question": "Quais são as principais partículas que compõem os anéis de Júpiter?",
             "options": [("a) Gelo, poeira e rochas", "a"), ("b) Rochas, poeira e gás", "b"), ("c) Gás, areia e rochas", "c"), ("d) Rochas, areia e água", "d")],
             "correct": "a"},
            
            {"question": "O _________ é o planeta mais próximo do sol. Complete:",
             "options": [("a) Terra", "a"), ("b) Vênus", "b"), ("c) Marte", "c"), ("d) Mercúrio", "d")],
             "correct": "d"},

            {"question": "O _________ é o planeta mais frio. Complete:",
             "options": [("a) Urano", "a"), ("b) Júpiter", "b"), ("c) Saturno", "c"), ("d) Mercúrio", "d")],
             "correct": "a"},
            
            {"question": "Quantas luas tem Saturno?",
             "options": [("a) 200 - 206", "a"), ("b) 56 - 62", "b"), ("c) 77 - 90", "c"), ("d) 140 - 147", "d")],
             "correct": "d"},

            {"question": "O núcleo interno do planeta __________ é sólido enquanto o núcleo externo é líquido. Complete:",
             "options": [("a) Vênus", "a"), ("b) Terra", "b"), ("c) Netuno", "c"), ("d) Marte", "d")],
             "correct": "b"},

            {"question": "Qual foi o planeta descoberto por cálculos matemáticos antes de ser observado visualmente?",
             "options": [("a) Vênus", "a"), ("b) Saturno", "b"), ("c) Netuno", "c"), ("d) Júpiter", "d")],
             "correct": "c"},

            {"question": "Qual o planeta que retém o calor do sol em suas nuvens espessas?",
             "options": [("a) Mercúrio", "a"), ("b) Vênus", "b"), ("c) Marte", "c"), ("d) Terra", "d")],
             "correct": "b"},
        ]
        self.current_question = 0
        self.score = 0
        self.show_result = False
        self.response = ""
        self.try_again = False
        self.go_to_menu = False
        self.try_again_rect = pygame.Rect(250, 400, 300, 50)
        self.go_to_menu_rect = pygame.Rect(250, 470, 300, 50)
        self.running = True
        self.alien = Alien('alien.png', self.WIDTH - 70, 50)# Criar o alienígena
        

    def draw_text(self, text, color, x, y, font_size=20):
        self.alien.draw(self.screen)
        font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def check_answer(self, answer):
        if self.current_question < len(self.questions):
            if self.questions[self.current_question]["correct"] == answer:
                self.score += 1
            self.show_result = True
            self.response = answer

    def reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.show_result = False

    def run(self):
        self.running = True
        while self.running:
            self.screen.fill(self.WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.check_answer('a')
                    elif event.key == pygame.K_b:
                        self.check_answer('b')
                    elif event.key == pygame.K_c:
                        self.check_answer('c')
                    elif event.key == pygame.K_d:
                        self.check_answer('d')
                
                elif self.current_question == len(self.questions):
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_clicked = pygame.mouse.get_pressed()[0]
                    print ("entra no elif ultima question")

                    if self.try_again_rect.collidepoint(mouse_pos):
                        if mouse_clicked:
                            self.try_again = True
                            print ("self.try_again = True")
                            self.running = False
                            
                    elif self.go_to_menu_rect.collidepoint(mouse_pos):
                        if mouse_clicked:
                            self.go_to_menu = True
                            print ("self.go_to_menu = True")
                            self.running = False
                            pygame.quit()
            # Exibir a pontuação atual com fonte menor
            self.draw_text(f"Score: {self.score}", self.BLACK, self.WIDTH - 150, 20, font_size=20)

            # Exibir a pergunta atual e as opções
            if self.current_question < len(self.questions) and not self.show_result:
                self.draw_text(self.questions[self.current_question]["question"], self.BLACK, 20, 20)
                options_y = 100
                for option, option_key in self.questions[self.current_question]["options"]:
                    color = self.BLACK
                    self.draw_text(option, color, 20, options_y)
                    options_y += 40

            # Exibir mensagem de resposta correta ou incorreta
            if self.show_result:
                if self.questions[self.current_question]["correct"] == self.response:
                    message = "Resposta correta!"
                    color = self.GREEN
                else:
                    message = "Resposta incorreta!"
                    color = self.RED
                self.draw_text(message, color, self.WIDTH // 2 - 100, self.HEIGHT - 50, font_size=30)

                # Aguardar 1 segundo antes de passar para a próxima pergunta
                pygame.display.flip()
                pygame.time.wait(1000)
                self.current_question += 1
                self.show_result = False

            # Mostrar o resultado final
            if self.current_question == len(self.questions):
                if self.score >= 6:
                    self.draw_text("Parabéns! Você foi aprovado!", self.GREEN, self.WIDTH // 2 - 150, self.HEIGHT // 2)
                else:
                    self.draw_text("Você não foi aprovado. Tente novamente!", self.RED, self.WIDTH // 2 - 200, self.HEIGHT // 2)
                
                # Desenhar os botões "Tentar Novamente" e "Voltar ao Menu"
                pygame.draw.rect(self.screen, self.BLACK, self.try_again_rect)
                pygame.draw.rect(self.screen, self.BLACK, self.go_to_menu_rect)
                self.draw_text("Tentar Novamente", self.WHITE, 275, 415)
                self.draw_text("Finalizar", self.WHITE, 305, 485)

            pygame.display.flip()
            self.clock.tick(60)

    def is_try_again(self):
        return self.try_again 
    
    def is_go_to_menu(self):
        return self.go_to_menu