from compomentes import botao

class botaoInicia:
    def __init__(self):
        self.selecaoDificudade = False
        self.tutorial = False
        self.tempo = 0

        self.inicia = botao((150,50),(325,150),'Inicia o jogo')
        self.tutorialClass = botao((150,50),(325,230),'Tutorial')

    def draw(self,surface):
        self.inicia.draw(surface)
        self.tutorialClass.draw(surface)