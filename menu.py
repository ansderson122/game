import pygame
from inimigo import inimigo1
from compomentes import *

class menu:
    def __init__(self,surface):
        self.fonte = pygame.font.Font(None, 25)
        self.surface = surface
        self.active = True 

        self.botaoSelecaoDificudade = selecaoDificudade()
        self.botaoInicia = botaoInicia()
        self.voceMorre = voceMorreu()
        self.animacaoMenu = animacaoMenu(self.surface)
        self.tutorialClass = tutorial(self.surface)

        self.velocidadeInimigo = 5
        self.selecaoDificudade = False
        self.tutorial = False
        self.tempo = 0

    def clickInicia(self):
        self.mouse = pygame.mouse.get_pos() 
        self.tempo += 1 

        if pygame.mouse.get_pressed()[0] and not self.selecaoDificudade and self.tempo > 20 :
            if  (self.mouse[0] >= 325 and self.mouse[0] <= 475) and (self.mouse[1] >= 150 and self.mouse[1] <= 200):
                self.tutorial = False
                self.selecaoDificudade = True
                self.tempo = 0
            elif  (self.mouse[0] >= 325 and self.mouse[0] <= 475) and (self.mouse[1] >= 230 and self.mouse[1] <= 280):
                self.tutorial = True
                self.selecaoDificudade = True
                self.tempo = 0   
        elif pygame.mouse.get_pressed()[0] and self.tempo > 20 and not self.tutorial:
            if  (self.mouse[0] >= 350 and self.mouse[0] <= 475) and (self.mouse[1] >= 150 and self.mouse[1] <= 200):
                self.active = False
                self.velocidadeInimigo = 5
                self.tempo = 0
            elif  (self.mouse[0] >= 325 and self.mouse[0] <= 475) and (self.mouse[1] >= 230 and self.mouse[1] <= 280):
                self.active = False
                self.velocidadeInimigo = 10
                self.tempo = 0

    def draw(self):
        self.clickInicia()
        if not self.selecaoDificudade:
            self.animacaoMenu.run()
            self.botaoInicia.draw(self.surface)
        elif self.tutorial:
            self.tutorialClass.draw()
            self.selecaoDificudade = not self.tutorialClass.fechaTutorial
        else:
            self.animacaoMenu.run()
            self.botaoSelecaoDificudade.draw(self.surface)

class voceMorreu:
    def __init__(self):
       self.texto = botao((0,0),(300,170),'Você Morreu',None,(25,20),100,"red")

    def draw(self,surface):
        self.texto.draw(surface)

class animacaoMenu:
    def __init__(self,surface):
        self.inimigo = inimigo1(surface)

        self.surface = surface
        self.imagem = pygame.image.load('graphics/Player/playerW1.png')
        self.rect = self.imagem.get_rect(midbottom = (80,300))
        self.player_gravidade = 5
        self.tempo = 0
        self.ok = True


    def player(self):
        self.rect.y += self.player_gravidade
        if self.rect.bottom >= 300: self.rect.bottom = 300
        self.surface.blit(self.imagem, self.rect) 
        
    def run(self):
        self.tempo += 1

        if self.tempo == 80 and self.ok:
            self.rect.y -= 180
            self.tempo = 0
            self.ok = False
        if self.tempo == 180:
            self.rect.y -= 180
            self.tempo = 0

        self.player()
        self.inimigo.update()