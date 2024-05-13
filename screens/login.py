import pygame
import json
from assets.player import Player

class LoginScreen:
    def __init__(self):
        self.dados_usuarios = self.dados_usuarios()
        self.font = pygame.font.Font(None, 36)
        self.input_rect = pygame.Rect(200, 350, 400, 50)
        self.input_text = ""
        self.error_message = ""
        self.info_message1 = "Digite seu nome de usuário."
        self.info_message2 = "Se for novo, um novo perfil será criado."
        self.is_done = False
        self.player = []

        # Carregar imagens de fundo para a tela de login
        self.background = pygame.image.load('login.jpg').convert()
        self.background = pygame.transform.scale(self.background, (800, 600))  # Redimensiona a imagem para preencher a tela

    def dados_usuarios(self):
        dados_usuarios = []
        try:
            with open("dados.json", "r") as file:
                dados_usuarios = json.load(file)
                print(dados_usuarios)
                return dados_usuarios
        except FileNotFoundError:
            print("O arquivo 'dados.json' não foi encontrado.")

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.validar_login(self.input_text):
                    # Transição para a tela do jogo após o login bem-sucedido
                    self.is_done = True
                    print("valida login com esse valor no input " + self.input_text)
                else:
                    self.error_message = "Nome de usuário não encontrado. Começando como novo jogador."
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def draw(self, screen):
        # Desenha a imagem de fundo
        screen.blit(self.background, (0, 0))

        # Desenha a mensagem informativa acima do campo de entrada
        info_surface1 = self.font.render(self.info_message1, True, (255, 255, 255))
        info_surface2 = self.font.render(self.info_message2, True, (255, 255, 255))
        screen.blit(info_surface1, (200, 200))
        screen.blit(info_surface2, (200, 240))

        # Desenha o campo de entrada e a mensagem de erro
        pygame.draw.rect(screen, (255, 255, 255), self.input_rect, 10, border_radius=5)
        text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        if self.error_message:
            error_surface = self.font.render(self.error_message, True, (255, 255, 255))
            screen.blit(error_surface, (300, 400))

    def validar_login(self, username):
        for player_data in self.dados_usuarios["players"]:
            if (player_data["username"] == username and player_data["username"] != ""):
                print(" entra no if de validar login ja existe.")
                # Criar o jogador com as informações do usuário existente
                self.player = Player(username, player_data["cards_unlocked"], player_data["level"])
                print(" valida login com esse valor no input ja existente : " + username)
                return self.player

        # Se não encontrou o usuário, criar um novo jogador
        print(" NAO entra no if de validar login ja existe.")

        # a primeira rodada é esse player quem joga infependente de ja existir ou n 
        # na real nao, a segunda rodada sempre cai aqui
        self.player = Player(username, [], 1)
        self.salvar_novo_jogador(username)

        print(" valida login com esse valor no input n existente" + username)
        return self.player

    def return_username(self):
        return self.username

    def salvar_novo_jogador(self, username):
        try:
            with open("dados.json", "r") as file:
                dados_usuarios = json.load(file)
                # Carrega o JSON atual
            # Verifica se o jogador já existe no JSON
            for player_data in dados_usuarios["players"]:
                if player_data["username"] == username:
                    return  # O jogador já existe, não é necessário fazer nada

            # Se o jogador não existe, cria um novo objeto de jogador
            novo_jogador = {
                "username": username,
                "level": 1,
                "cards_unlocked": [
                ]
            }
            print(novo_jogador)

            # Adiciona o novo jogador à lista de jogadores
            dados_usuarios["players"].append(novo_jogador)

            # Salva o JSON atualizado de volta no arquivo
            with open("dados.json", "w") as file:
                json.dump(dados_usuarios, file)

        except FileNotFoundError:
            print("O arquivo 'dados.json' não foi encontrado.")
        except json.JSONDecodeError:
            print("Houve um erro ao decodificar o JSON.")
