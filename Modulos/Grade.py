import pygame
import random

# Importa a classe Cores para obter as cores das células
class Grade:
    def __init__(self):
        # Inicializa as propriedades do objeto Grade
        self.num_linhas = 20
        self.num_colunas = 10
        self.tamanho_celula = 30
        # Cria uma matriz para representar a grade, preenchida com zeros
        self.grade = [[0 for j in range(self.num_colunas)] for i in range(self.num_linhas)]
        # Obtém as cores das células da classe Cores
        self.cores = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Imprime o estado atual da grade
    def imprimir_grade(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                print(self.grade[linha][coluna], end=" ")
            print()

    # Verifica se uma posição (linha, coluna) está dentro da grade
    def esta_dentro(self, linha, coluna):
        if linha >= 0 and linha < self.num_linhas and coluna >= 0 and coluna < self.num_colunas:
            return True
        return False

    # Verifica se uma célula está vazia
    def esta_vazia(self, linha, coluna):
        if self.grade[linha][coluna] == 0:
            return True
        return False

    # Verifica se uma linha está completamente preenchida
    def linha_esta_cheia(self, linha):
        for coluna in range(self.num_colunas):
            if self.grade[linha][coluna] == 0:
                return False
        return True

    # Limpa uma linha preenchida
    def limpar_linha(self, linha):
        for coluna in range(self.num_colunas):
            self.grade[linha][coluna] = 0

    # Move uma linha para baixo, usado ao limpar linhas completas
    def mover_linha_baixo(self, linha, num_linhas):
        for coluna in range(self.num_colunas):
            self.grade[linha + num_linhas][coluna] = self.grade[linha][coluna]
            self.grade[linha][coluna] = 0

    # Limpa as linhas completamente preenchidas e move as linhas acima para baixo
    def limpar_linhas_completas(self):
        completadas = 0
        for linha in range(self.num_linhas - 1, 0, -1):
            if self.linha_esta_cheia(linha):
                self.limpar_linha(linha)
                completadas += 1
            elif completadas > 0:
                self.mover_linha_baixo(linha, completadas)
        return completadas

    # Reinicia a grade, preenchendo-a com zeros
    def reiniciar(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                self.grade[linha][coluna] = 0

    # Desenha a grade na tela usando a biblioteca Pygame
    def desenhar(self, tela):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                # Obtém o valor da célula e cria um retângulo correspondente
                valor_celula = self.grade[linha][coluna]
                retangulo_celula = pygame.Rect(coluna * self.tamanho_celula + 11, linha * self.tamanho_celula + 11,
                                               self.tamanho_celula - 1, self.tamanho_celula - 1)
                # Desenha o retângulo colorido na tela
                pygame.draw.rect(tela, self.cores, retangulo_celula)
