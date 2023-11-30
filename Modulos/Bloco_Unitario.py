import pygame
from Posicao import Posicao

# Importa a classe Cores para obter as cores das células
class Bloco:
    def __init__(self, id):
        # Inicializa as propriedades do objeto Bloco
        self.id = id
        self.celulas = {
            0: [(0, 0), (0, 1), (0, 2), (0, 3)],  # Exemplo para um bloco linear
            # Adicione outras chaves conforme necessário para outros blocos
        }
        self.tamanho_celula = 30
        self.deslocamento_linha = 0
        self.deslocamento_coluna = 0
        self.estado_rotacao = 0
        # Obtém as cores das células da classe Cores
        self.cores = Cores.obter_cor_celula()

    # Move o bloco por um número especificado de linhas e colunas
    def mover(self, linhas, colunas):
        self.deslocamento_linha += linhas
        self.deslocamento_coluna += colunas

    # Obtém as posições das células do bloco após o movimento
    def pegar_posicoes_celula(self):
        azulejos = self.celulas[self.estado_rotacao]
        azulejos_movidos = []
        for posicao in azulejos:
            # Certifique-se de que posicao seja uma instância da classe Posicao
            if isinstance(posicao, tuple):
                posicao = Posicao(posicao[0], posicao[1])

            # Agora você pode acessar corretamente linha e coluna
            nova_posicao = Posicao(posicao.linha + self.deslocamento_linha, posicao.coluna + self.deslocamento_coluna)
            azulejos_movidos.append(nova_posicao)
        return azulejos_movidos

    # Rotaciona o bloco no sentido horário
    def rotacionar(self):
        self.estado_rotacao += 1
        if self.estado_rotacao == len(self.celulas):
            self.estado_rotacao = 0

    # Desfaz a rotação do bloco
    def desfazer_rotacao(self):
        self.estado_rotacao -= 1
        if self.estado_rotacao == -1:
            self.estado_rotacao = len(self.celulas) - 1

    # Desenha o bloco na tela usando a biblioteca Pygame
    def desenhar(self, tela, deslocamento_x, deslocamento_y):
        azulejos = self.pegar_posicoes_celula()
        for azulejo in azulejos:
            # Cria um retângulo para cada célula do bloco e desenha na tela
            retangulo_azulejo = pygame.Rect(deslocamento_x + azulejo.coluna * self.tamanho_celula,
                                            deslocamento_y + azulejo.linha * self.tamanho_celula, self.tamanho_celula - 1, self.tamanho_celula - 1)
            pygame.draw.rect(tela, self.cores[self.id], retangulo_azulejo)

#Classe para definir as cores
class Cores:
    # Definição de cores como atributos da classe
    cinza = (211,211,211)
    verde = (47, 230, 23)
    vermelho = (232, 18, 18)
    laranja = (226, 116, 17)
    amarelo = (237, 234, 4)
    roxo = (166, 0, 247)
    ciano = (21, 204, 209)
    azul = (13, 64, 216)
    branco = (255, 255, 255)
    azul_escuro = (44, 44, 127)
    azul_claro = (59, 85, 162)

    # Método de classe para obter a lista de cores
    @classmethod
    def obter_cor_celula(cls):
        return [cls.cinza, cls.verde, cls.vermelho, cls.laranja, cls.amarelo, cls.roxo, cls.ciano, cls.azul]
