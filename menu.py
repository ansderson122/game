import pygame
from inimigo import inimigo1

class menu:
    def __init__(self,surface):
        self.fonte = pygame.font.Font(None, 25)
        self.surface = surface
        self.active = True 
        self.selecaoDificudade = False

        self.botaoSelecaoDificudade = selecaoDificudade()
        self.botaoInicia = botaoInicia()
        self.voceMorre = voceMorreu()
        self.animacaoMenu = animacaoMenu(self.surface)

        self.velocidadeInimigo = 0
        self.tempo = 0


    def clickInicia(self):
        self.mouse = pygame.mouse.get_pos() 
        event = pygame.event.get()

        self.tempo += 1 

        if pygame.mouse.get_pressed()[0] and not self.selecaoDificudade and self.tempo > 20 :
            if  (self.mouse[0] >= 325 and self.mouse[0] <= 475) and (self.mouse[1] >= 150 and self.mouse[1] <= 200):
                self.selecaoDificudade = True
                self.tempo = 0
        elif pygame.mouse.get_pressed()[0] and self.tempo > 20 :
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
        else:
            self.animacaoMenu.run()
            self.botaoSelecaoDificudade.draw(self.surface)




class botaoInicia:
    def __init__(self):
        self.fonte =  pygame.font.Font(None, 25)


    def draw(self,surface):
        self.inicia = pygame.Surface((150,50))
        self.inicia.fill('white')
        self.iniciaRect = self.inicia.get_rect(topleft = (325,150))

        score_surf = self.fonte.render('Inicia o jogo', False, (0,0,0))
        score_rect = score_surf.get_rect(topleft = (350,170))
        
        
        surface.blit(self.inicia,self.iniciaRect)
        surface.blit(score_surf, score_rect)

class selecaoDificudade:
    def __init__(self):
        self.fonte =  pygame.font.Font(None, 25)

    def draw(self,surface):
        self.normalCaixa = pygame.Surface((150,50))
        self.normalCaixa .fill('white')
        self.normalRect = self.normalCaixa .get_rect(topleft = (325,150))

        self.dificilCaixa = pygame.Surface((150,50))
        self.dificilCaixa.fill('white')
        self.dificilRect = self.dificilCaixa.get_rect(topleft = (325,230))


        surface.blit(self.normalCaixa ,self.normalRect)
        surface.blit(self.dificilCaixa,self.dificilRect)

        score_surf = self.fonte.render('Normal', False, (0,0,0))
        score_rect = score_surf.get_rect(topleft = (350,170))       
        surface.blit(score_surf, score_rect)        
        
        score_surf1 = self.fonte.render('Difícil', False, (0,0,0))
        score_rect1 = score_surf1.get_rect(topleft = (350,250))
        surface.blit(score_surf1, score_rect1)

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
