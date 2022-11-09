import pygame

class menu:
    def __init__(self,surface):
        self.fonte = pygame.font.Font(None, 25)
        self.surface = surface
        self.active = True 
        self.selecaoDificudade = False

        self.botaoSelecaoDificudade = selecaoDificudade()
        self.botaoInicia = botaoInicia()
        


    def clickInicia(self):
        self.mouse = pygame.mouse.get_pos() 
        event = pygame.event.wait()

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not self.selecaoDificudade :
            if  (self.mouse[0] >= 325 and self.mouse[0] <= 475) and (self.mouse[1] >= 150 and self.mouse[1] <= 200):
                self.selecaoDificudade = True
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] :
            if  (self.mouse[0] >= 350 and self.mouse[0] <= 475) and (self.mouse[1] >= 150 and self.mouse[1] <= 200):
                self.active = False
            elif  (self.mouse[0] >= 325 and self.mouse[0] <= 475) and (self.mouse[1] >= 230 and self.mouse[1] <= 280):
                self.active = False

    def draw(self):
        self.clickInicia()
        if not self.selecaoDificudade:
            self.botaoInicia.draw(self.surface)
        else:
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