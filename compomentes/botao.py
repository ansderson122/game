import pygame

class botao:
    #dis é as dimenção, pos é a posição , tex para alinhamento do texto
    def __init__(self,dis,pos=(0,0),texto="",corFundo='white', tex = (25,20),tamFonte= 25,texCor = "black" ):
        self.fundo = fundo(dis,pos,corFundo)
        self.fonte =  pygame.font.Font(None, tamFonte)

        self.texto = self.fonte.render(texto, False, texCor)
        self.texto_rect = self.texto.get_rect(topleft = (pos[0]+tex[0],pos[1]+tex[1]))

    def draw(self,surface):
        self.fundo.draw(surface)
        surface.blit(self.texto, self.texto_rect)

class fundo:
    def __init__(self,dis = (0,0),pos = (0,0), cor = 'white'):
        self.quadrado = pygame.Surface(dis)
        if cor != None: self.quadrado.fill(cor)
        self.quadradoRect = self.quadrado.get_rect(topleft = pos)

    def draw(self,surface):
        surface.blit(self.quadrado,self.quadradoRect)