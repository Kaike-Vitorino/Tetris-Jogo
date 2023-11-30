import sys
from logica_game import *

pygame.init()

# Configuracao da fonte e superficies de texto.
fonte_titulo = pygame.font.Font(None, 40)

superficie_pontuacao = fonte_titulo.render("Pontos", True, Cores.branco)
superficie_proximo = fonte_titulo.render("Prox", True, Cores.branco)
superficie_game_over = fonte_titulo.render("Acabou o jogo", True, Cores.branco)

# Posicoes e dimensoes dos retangulos
retangulo_pontuacao = pygame.Rect(320, 55, 170, 60)
retangulo_proximo = pygame.Rect(320, 215, 170, 180)

# Configuracao da tela
tela = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Relogio para controlar a taxa de quadros
relogio = pygame.time.Clock()

# Instancia do jogo
jogo = Jogo()

# Evento personalizado para atualizacao do jogo
ATUALIZAR_JOGO = pygame.USEREVENT
pygame.time.set_timer(ATUALIZAR_JOGO, 200)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if jogo.jogo_acabou == True:
                jogo.jogo_acabou = False
                jogo.reiniciar()
            if evento.key == pygame.K_LEFT and jogo.jogo_acabou == False:
                jogo.mover_esquerda()
            if evento.key == pygame.K_RIGHT and jogo.jogo_acabou == False:
                jogo.mover_direita()
            if evento.key == pygame.K_DOWN and jogo.jogo_acabou == False:
                jogo.mover_baixo()
                jogo.atualizar_pontuacao(0, 1)
            if evento.key == pygame.K_UP and jogo.jogo_acabou == False:
                jogo.rotacionar()
        if evento.type == ATUALIZAR_JOGO and jogo.jogo_acabou == False:
            jogo.mover_baixo()

    # Desenho
    superficie_valor_pontuacao = fonte_titulo.render(str(jogo.pontuacao), True, Cores.branco)

    tela.fill(Cores.ciano)
    tela.blit(superficie_pontuacao, (365, 20, 50, 50))
    tela.blit(superficie_proximo, (375, 180, 50, 50))

    if jogo.jogo_acabou == True:
        tela.blit(superficie_game_over, (320, 450, 50, 50))

    pygame.draw.rect(tela, Cores.azul_escuro, retangulo_pontuacao, 0, 10)
    tela.blit(superficie_valor_pontuacao, superficie_valor_pontuacao.get_rect(centerx=retangulo_pontuacao.centerx,
                                                                               centery=retangulo_pontuacao.centery))
    pygame.draw.rect(tela, Cores.azul_escuro, retangulo_proximo, 0, 10)
    jogo.desenhar(tela)

    pygame.display.update()
    relogio.tick(60)
