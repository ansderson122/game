import pygame 
from inimigo import inimigo1
from player import player
from menu import menu

class level():
    def __init__(self, surface):
        self.surface = surface
        self.ceu =  pygame.image.load('graphics/Tela/ceu.png').convert()
        self.terra = pygame.image.load('graphics/Tela/terra.png').convert()

        self.numNivel = 0
        self.tempoInicial = 0
        self.fonte = pygame.font.Font(None, 50)
        self.game_active = True

        self.inimigo1 = inimigo1(self.surface)
        self.player = player(self.surface)
        self.menu = menu(self.surface)
        

    def display_score(self):
        self.timer = int((pygame.time.get_ticks())/1000 - self.tempoInicial)
        score_surf = self.fonte.render(f'Time: {self.timer}', False, (0,0,0))
        score_rect = score_surf.get_rect(center = (400,50))
        self.surface.blit(score_surf, score_rect)


       
        if self.timer%5 == 0 and self.timer != 0:
            self.numNivel+=(1/60) 
        else:
            self.numNivel
        nivel = self.fonte.render(f'Nivel: {int(self.numNivel)}', False, (0,0,0))
        nivelRect = nivel.get_rect(center = (700,50))
        self.surface.blit(nivel, nivelRect)

    def colliderect1(self):
        if self.inimigo1.rect.colliderect(self.player.rect):
            self.menu.voceMorre.draw(self.surface)
            self.game_active = False


    def setup_level(self):
        self.surface.blit(self.ceu,(0,0))
        self.surface.blit(self.terra,(0,300))

    def morte(self):
        event = pygame.event.wait()
        if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and ( event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_UP) :
            self.game_active = True
            self.inimigo1.rect.left = 800
            self.tempoInicial = int((pygame.time.get_ticks())/1000)
            self.inimigo1.velocidade = self.menu.velocidadeInimigo
            self.numNivel = 0

            self.menu.active = True
            self.menu.selecaoDificudade = False
    
    def retornaMenu(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            self.menu.active = True
    
        
    def run(self):
        
        if not self.game_active:
            self.morte()
        elif self.menu.active:
            self.setup_level()
            self.menu.draw()
            self.inimigo1.velocidade = self.menu.velocidadeInimigo
            self.tempoInicial = int((pygame.time.get_ticks())/1000)
        else :
            self.setup_level()
            self.display_score()

            self.inimigo1.update()
            self.inimigo1.alteraVelocidade(self.timer)

            self.player.update()
            
            self.colliderect1()
            self.retornaMenu()
            