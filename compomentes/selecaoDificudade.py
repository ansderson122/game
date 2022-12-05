import pygame
from compomentes import botao

class selecaoDificudade:
    def __init__(self):
        self.normal = botao((150,50),(325,150),'Normal')
        self.dificil = botao((150,50),(325,230),'Difícil')

    def draw(self,surface):
        self.normal.draw(surface)
        self.dificil.draw(surface)
