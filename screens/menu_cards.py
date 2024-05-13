import pygame
import sys

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
GREEN = (0, 255, 0)
PINK =  (217, 0, 190)


class Menu_Cards:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 36)
        self.title_text = self.title_font.render("Parabéns! Agora estude seus cards", True, WHITE)
        self.cards_texts = [
            ("Mercúrio",
             "* É o planeta mais próximo do sol",
             "* Durante o dia, a temperatura pode chegar a cerca de 430°C, enquanto à noite pode cair para -180°C.",
             "* Mercúrio possui uma superfície marcada por crateras de impacto, desfiladeiros e planícies vulcânicas.",
             "* Mercúrio completa uma órbita ao redor do Sol em aproximadamente 88 dias terrestres.",
             "* Mercúrio é o menor planeta do Sistema Solar"),
            ("Vênus",
             "* Retém o calor do sol em suas nuvens espessas",
             "* Vênus possui uma temperatura média de superfície de cerca de 462°C, tornando-a o planeta mais quente do Sistema Solar.",
             "* Leva cerca de 243 dias terrestres para completar uma rotação completa",
             "* Vênus possui uma atmosfera extremamente densa composta principalmente de dióxido de carbono, com nuvens de ácido sulfúrico",
             "* Chamado de 'gêmea da Terra' devido ao seu tamanho e composição semelhantes"),
            ("Terra",
             "* O Oceano Pacífico é o mais extenso do planeta, cobrindo um terço de sua superfície.",
             "* Aproximadamente 71% da superfície terrestre é coberta por água.",
             "* O núcleo interno do planeta é sólido enquanto o núcleo externo é líquido",
             "* Ígneas, sedimentares e metamórficas são os três tipos principais de rochas encontradas na crosta terrestre",
             "* O núcleo é a camada mais interna da Terra, composto principalmente de ferro e níquel."),
            ("Marte",
             "* Monte Olimpo, maior vulcão conhecido no sistema solar, se localiza em Marte, com 21.9 quilômetros de altura.",
             "* A temperatura do planeta varia de -125°C a 20°C, tornando-o um ambiente extremo.",
             "* Sua atmosfera é composta de dióxido de carbono, com traços de nitrogênio e argônio",
             "* O planeta pode conter pistas sobre a origem da vida e oferecer insights sobre a habitabilidade de outros planetas.",
             "* Sondas robóticas, orbitadores e missões tripuladas planejadas para futuro, são tipos de missões espaciais enviadas para Marte."),
            ("Júpiter",
             "* As principais partículas que compõem os anéis de Júpiter são: Gelo, poeira e rochas",
             "* É o maior planeta do Sistema Solar",
             "* Possui faixas atmosféricas coloridas e uma Grande Mancha Vermelha, uma tempestade gigante que dura séculos",
             "* Io, Europa, Ganimedes e Calisto, conhecidas como as Luas de Galileu e são as quatro maiores luas do planeta.",
             "* Júpiter completa uma órbita em torno do Sol em aproximadamente 12 anos terrestres."),
            ("Saturno",
             "* Possui 145 luas",
             "* Leva aproximadamente 29 anos terrestres para completar uma órbita ao redor do Sol.",
             "* Saturno tem um período de rotação muito rápido, girando em torno de seu eixo em cerca de 10,7 horas terrestres.",
             "* Os anéis de Saturno são compostos de partículas de gelo e poeira que refletem a luz solar, tornando-os visíveis mesmo através de pequenos telescópios.",
             "* Saturno é cerca de 9,5 vezes maior em diâmetro do que a Terra"),
            ("Urano",
             "* É o planeta mais frio",
             "* Urano leva cerca de 84 anos terrestres para completar uma órbita completa ao redor do Sol.",
             "* Miranda, Ariel, Umbriel, Titânia e Oberon são as cinco maiores luas de Urano.",
             "* É um gigante de gelo, composto principalmente de hidrogênio e hélio",
             "* A temperatura média da atmosfera superior de Urano é de aproximadamente -210°C."),
            ("Netuno",
             "* Foi o planeta descoberto por cálculos matemáticos antes de ser observado visualmente.",
             "* Leva aproximadamente 165 anos terrestres para completar uma órbita ao redor do Sol.",
             "* Tritão é a maior lua de Netuno e uma das mais intrigantes, com uma atmosfera fina e geisers de nitrogênio ativos em sua superfície",
             "* Possui uma temperatura média de cerca de -200°C.",
             "* A Grande Mancha Escura é uma tempestade gigantesca na atmosfera de Netuno, semelhante à Grande Mancha Vermelha de Júpiter"),
        ]
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.scroll_pos = 0
        self.scroll_speed = 5
        self.scroll_up = False
        self.scroll_down = False
        self.continue_text = self.font.render("Ir para o Quiz", True, WHITE)
        self.continue_rect = self.continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

        # Carregar imagem de fundo
        self.background_image = pygame.image.load('login.jpg').convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cards_surface = pygame.Surface((SCREEN_WIDTH - 80, SCREEN_HEIGHT - 130))
        self.cards_rect = self.cards_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        self.start_quiz = False
        

    def draw(self, surface):
        # Desenhar imagem de fundo
        surface.blit(self.background_image, (0, 0))

        # Desenhar texto e botões
        surface.blit(self.title_text, self.title_rect)

        # Desenhar os cards
        self.cards_surface.fill(PINK)
        card_y = 10 - self.scroll_pos
        for card_text in self.cards_texts:
            card_rect = pygame.Rect(10, card_y, self.cards_rect.width - 20, 140)
            pygame.draw.rect(self.cards_surface, WHITE, card_rect, 2)
            for line in card_text:
                text = self.font.render(line, True, WHITE)
                text_rect = text.get_rect(topleft=(20, card_y))
                self.cards_surface.blit(text, text_rect)
                card_y += text_rect.height + 5
            card_y += 10
            if card_y - self.scroll_pos > self.cards_rect.height:
                break

        surface.blit(self.cards_surface, self.cards_rect)

        # Desenhar botão de "Ir para o Quiz"
        pygame.draw.rect(surface, WHITE, self.continue_rect, 2)
        surface.blit(self.continue_text, self.continue_rect)

    def update(self):
        self.scroll_up = False
        self.scroll_down = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        if self.continue_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                self.start_quiz = True
                return True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.scroll_up = True
        elif keys[pygame.K_DOWN]:
            self.scroll_down = True

        # Atualize a posição de rolagem
        if self.scroll_up:
            self.scroll_pos = max(self.scroll_pos - self.scroll_speed, 0)
            self.scroll_up = False
        elif self.scroll_down:
            self.scroll_pos = min(self.scroll_pos + self.scroll_speed, len(self.cards_texts) * 300 - self.cards_rect.height)
            self.scroll_down = False

        return False
    
    def quiz(self):
        return self.start_quiz