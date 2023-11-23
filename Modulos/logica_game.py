import pygame
from Grade import *
from Blocos_Formatos import *
import random

# Classe que representa o jogo
class Jogo:
    def __init__(self):
        # Inicialização do jogo
        self.grade = Grade()  # Instância da grade
        self.blocos = [Bloco_em_I(), Bloco_em_J(), Bloco_em_L(), Bloco_em_O(), Bloco_em_S(), Bloco_em_T(), Bloco_em_Z()]  # Lista de blocos
        self.bloco_atual = self.get_bloco_aleatorio()  # Bloco atual
        self.proximo_bloco = self.get_bloco_aleatorio()  # Próximo bloco
        self.jogo_acabou = False  # Flag para indicar se o jogo acabou
        self.pontuacao = 0  # Pontuação do jogador
        '''
        self.som_rotacao = pygame.mixer.Sound("Sounds/rotate.ogg")  # Som de rotação
        self.som_limpar = pygame.mixer.Sound("Sounds/clear.ogg")  # Som de linha completa

        pygame.mixer.music.load("Sounds/music.ogg")  # Carregar música de fundo
        pygame.mixer.music.play(-1)  # Reproduzir música em loop
        '''

    def atualizar_pontuacao(self, linhas_limpar, pontos_mover_baixo):
        # Atualizar pontuação com base no número de linhas eliminadas e pontos de movimento para baixo
        if linhas_limpar == 1:
            self.pontuacao += 100
        elif linhas_limpar == 2:
            self.pontuacao += 300
        elif linhas_limpar == 3:
            self.pontuacao += 500
        self.pontuacao += pontos_mover_baixo

    def get_bloco_aleatorio(self):
        # Obter um bloco aleatório da lista e removê-lo da lista
        if len(self.blocos) == 0:
            self.blocos = [Bloco_em_I(), Bloco_em_J(), Bloco_em_L(), Bloco_em_O(), Bloco_em_S(), Bloco_em_T(), Bloco_em_Z()]
        bloco = random.choice(self.blocos)
        self.blocos.remove(bloco)
        return bloco

    def mover_esquerda(self):
        # Mover o bloco para a esquerda
        self.bloco_atual.mover(0, -1)
        if self.bloco_dentro() == False or self.bloco_cabe() == False:
            self.bloco_atual.mover(0, 1)

    def mover_direita(self):
        # Mover o bloco para a direita
        self.bloco_atual.mover(0, 1)
        if self.bloco_dentro() == False or self.bloco_cabe() == False:
            self.bloco_atual.mover(0, -1)

    def mover_baixo(self):
        # Mover o bloco para baixo
        self.bloco_atual.mover(1, 0)
        if self.bloco_dentro() == False or self.bloco_cabe() == False:
            self.bloco_atual.mover(-1, 0)
            self.travar_bloco()

    def travar_bloco(self):
        # Travar o bloco atual na grade
        azulejos = self.bloco_atual.get_posicoes_celula()
        for posicao in azulejos:
            self.grade.grade[posicao.linha][posicao.coluna] = self.bloco_atual.id
        self.bloco_atual = self.proximo_bloco
        self.proximo_bloco = self.get_bloco_aleatorio()
        linhas_completas = self.grade.limpar_linhas_completas()
        if linhas_completas > 0:
            self.som_limpar.play()
            self.atualizar_pontuacao(linhas_completas, 0)
        if self.bloco_cabe() == False:
            self.jogo_acabou = True

    def reiniciar(self):
        # Reiniciar o jogo
        self.grade.reiniciar()
        self.blocos = [Bloco_em_I(), Bloco_em_J(), Bloco_em_L(), Bloco_em_O(), Bloco_em_S(), Bloco_em_T(), Bloco_em_Z()]
        self.bloco_atual = self.get_bloco_aleatorio()
        self.proximo_bloco = self.get_bloco_aleatorio()
        self.pontuacao = 0

    def bloco_cabe(self):
        # Verificar se o bloco cabe na grade
        azulejos = self.bloco_atual.get_posicoes_celula()
        for azulejo in azulejos:
            if self.grade.esta_vazia(azulejo.linha, azulejo.coluna) == False:
                return False
        return True

    def rotacionar(self):
        # Rotacionar o bloco atual
        self.bloco_atual.rotacionar()
        if self.bloco_dentro() == False or self.bloco_cabe() == False:
            self.bloco_atual.desfazer_rotacao()
        else:
            self.som_rotacao.play()

    def bloco_dentro(self):
        # Verificar se todas as células do bloco estão dentro da grade
        azulejos = self.bloco_atual.get_posicoes_celula()
        for azulejo in azulejos:
            if self.grade.esta_dentro(azulejo.linha, azulejo.coluna) == False:
                return False
        return True

    def desenhar(self, tela):
        # Desenhar a grade, bloco atual e próximo bloco na tela
        self.grade.desenhar(tela)
        self.bloco_atual.desenhar(tela, 11, 11)

        if self.proximo_bloco.id == 3:
            self.proximo_bloco.desenhar(tela, 255, 290)
        elif self.proximo_bloco.id == 4:
            self.proximo_bloco.desenhar(tela, 255, 280)
        else:
            self.proximo_bloco.desenhar(tela, 270, 270)
