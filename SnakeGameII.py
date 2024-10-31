import pygame
import random

pygame.init()

largura, altura = 600, 400
cor_fundo = (30, 30, 30)  
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)
tamanho_bloco = 20
velocidade = 10

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha - Dark Mode")

relogio = pygame.time.Clock()

def posicao_aleatoria():
    x = random.randint(0, (largura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
    y = random.randint(0, (altura - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
    return x, y

def desenhar_cobra(tela, cobra_lista):
    for bloco in cobra_lista:
        pygame.draw.rect(tela, cor_cobra, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

def verificar_bordas(x, y):
    if x >= largura:
        x = 0
    elif x < 0:
        x = largura - tamanho_bloco
    if y >= altura:
        y = 0
    elif y < 0:
        y = altura - tamanho_bloco
    return x, y
def jogo():
    
    fim_jogo = False
    x, y = largura // 2, altura // 2  
    velocidade_x, velocidade_y = 0, 0
    cobra_lista = []
    comprimento_cobra = 1

    comida_x, comida_y = posicao_aleatoria()

    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -tamanho_bloco
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = tamanho_bloco
                    velocidade_y = 0
                elif evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_y = -tamanho_bloco
                    velocidade_x = 0
                elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_y = tamanho_bloco
                    velocidade_x = 0

        x += velocidade_x
        y += velocidade_y
        x, y = verificar_bordas(x, y)

        cobra_cabeca = [x, y]
        cobra_lista.append(cobra_cabeca)
        if len(cobra_lista) > comprimento_cobra:
            del cobra_lista[0]

        for bloco in cobra_lista[:-1]:
            if bloco == cobra_cabeca:
                fim_jogo = True

        if x == comida_x and y == comida_y:
            comida_x, comida_y = posicao_aleatoria()
            comprimento_cobra += 1

        tela.fill(cor_fundo)
        pygame.draw.rect(tela, cor_comida, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        desenhar_cobra(tela, cobra_lista)

        pygame.display.update()
        relogio.tick(velocidade)

    pygame.quit()

jogo()