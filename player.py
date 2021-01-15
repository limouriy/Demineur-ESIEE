import pygame

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24) #changement de la taille de la police

class Player: #dans cette classe on va donner 5 vies au joueur et chaque fois qu'il meurs on fait une substraction de -1
    def __init__(self):
        self.health = 5

    def sub_health(self):
        self.health -= 1

    def get_health(self):
        return self.health


class Stats:
    @staticmethod
    def draw(surface, label, pos):
        textsurface = myfont.render(label, False, (255, 255, 255))
        surface.blit(textsurface, (pos[0], pos[1]))