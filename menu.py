import pygame
from inimigo import inimigo1
from compomentes.botao import botao

class menu:
    def __init__(self,surface):
        self.fonte = pygame.font.Font(None, 25)
        self.surface = surface

        self.active = True 
        self.selecaoDificudade = False
        self.tutorial = False

        self.botaoSelecaoDificudade = selecaoDificudade()
        self.botaoInicia = botaoInicia()
        self.voceMorre = voceMorreu()
        self.animacaoMenu = animacaoMenu(self.surface)
        self.tutorialClass = tutorial(self.surface)

        self.velocidadeInimigo = 0
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

class botaoInicia:
    def __init__(self):
        self.inicia = botao((150,50),(325,150),'Inicia o jogo')
        self.tutorial = botao((150,50),(325,230),'Tutorial')
        
    def draw(self,surface):
        self.inicia.draw(surface)
        self.tutorial.draw(surface)

class tutorial:
    def __init__(self,surface):
        self.volta = botao((80,30),(0,0),"Volta",'white',(25,7))
        self.surface = surface
        self.fechaTutorial = False
        self.textos = [
            "Controle:",
            "Pressione W para pular",
            "Pressione S para descer mais rapido",
            "Pressione UP para pular",
            "Pressione DOWN para descer mais rapido",
            "Pressione o botao esquerdo do mouse para pular",
            "Pressione o botao direito do mouse para descer mais rapido",
            "Pressione SPACE para pular",
        ]

    def clickVolta(self):
        self.mouse = pygame.mouse.get_pos() 
        if pygame.mouse.get_pressed()[0]:
            if  (self.mouse[0] >= 0 and self.mouse[0] <= 80) and (self.mouse[1] >= 0 and self.mouse[1] <= 30):
                self.fechaTutorial = True

    def draw(self):
        self.fechaTutorial = False
        self.volta.draw(self.surface)

        self.texto = botao((0,0),(50,50),"Objetivo é não colide com os inimigos",None,(25,20),35)
        self.texto.draw(self.surface)

        con = 120
        for i in self.textos:
            self.texto = botao((0,0),(50,con),i,None,(25,20),35)
            self.texto.draw(self.surface)
            con+=30
   
        self.clickVolta()

    

class selecaoDificudade:
    def __init__(self):
        self.normal = botao((150,50),(325,150),'Normal')
        self.dificil = botao((150,50),(325,230),'Difícil')
       

    def draw(self,surface):
       self.normal.draw(surface)
       self.dificil.draw(surface)


class voceMorreu:
    def __init__(self) -> None:
        self.fonte =  pygame.font.Font(None, 100)

    def draw(self,surface):
        score_surf = self.fonte.render('Você Morreu', False, 'red')
        score_rect = score_surf.get_rect(topleft = (300,170))       
        surface.blit(score_surf, score_rect)

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