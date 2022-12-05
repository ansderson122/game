import pygame
from compomentes import botao

class tutorial:
    def __init__(self,surface):
        self.volta = botao((80,30),(0,0),"Volta",'white',(25,7))
        self.surface = surface
        self.fechaTutorial = False
        self.textos = [
            "Objetivo é não colide com os inimigos",
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

        con = 50
        for i in self.textos:
            self.texto = botao((0,0),(50,con),i,None,(25,20),35)
            self.texto.draw(self.surface)
            con+=30
   
        self.clickVolta()
