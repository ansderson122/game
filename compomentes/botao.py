import pygame

class botao:
    #dis é as dimenção, pos é a posição 
    def __init__(self,dis,pos=(0,0),texto="",corFundo='white'):
        self.fundo = quadrado(dis,pos,corFundo)
        self.fonte =  pygame.font.Font(None, 25)

        self.texto = self.fonte.render(texto, False, (0,0,0))
        self.texto_rect = self.texto.get_rect(topleft = (pos[0]+25,pos[1]+20))

    def draw(self,surface):
        self.fundo.draw(surface)
        surface.blit(self.texto, self.texto_rect)



class quadrado:
    #dis é as dimenção do quadrado, pos é a posição 
    def __init__(self,dis = (0,0),pos = (0,0), cor = 'white'):
        self.quadrado = pygame.Surface(dis)
        self.quadrado.fill(cor)
        self.quadradoRect = self.quadrado.get_rect(topleft = pos)

    def draw(self,surface):
        surface.blit(self.quadrado,self.quadradoRect)