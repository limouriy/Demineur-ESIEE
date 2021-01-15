import pygame
from board import Grid
from player import Player, Stats
from enum import Enum, auto  #Enum (énumération) est une classe basique pour la création de constantes énumérées
     
        

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,100) #pour positionner la fenêtre sur l'écran à la position (400,100)

surface = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Démineur')


class States(Enum):
    parcourir = auto()
    jeu_fini = auto()
    gagne = auto()

state = States.parcourir

player = Player()
grid = Grid(player)

parcourir = True

while parcourir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            parcourir = False
        if event.type == pygame.MOUSEBUTTONDOWN and state == States.parcourir:
            if pygame.mouse.get_pressed()[0]: # checker une mine par le boutton gauche de la souris 
                pos = pygame.mouse.get_pos()
                grid.clique(pos[0], pos[1])
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                grid.marquer_mine(pos[0]//30, pos[1]//30)
            if grid.check_if_win():
                state = States.gagne
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (state == States.jeu_fini or state == States.gagne):
                grid.recharger()
                state = States.parcourir
            if event.key == pygame.K_a:
                grid.montrer_mine()

    surface.fill((0,0,0))

    if player.get_health()== 0:    # si le nombre de vies devient nul
        state = States.jeu_fini      # alors on affiche game over ( le jeu est terminée)

    if state == States.jeu_fini: #ici on montre ce qu'on peu faire aprés un jeu perdu
        Stats.draw(surface, 'Le jeu est terminé!', (970, 300))
        Stats.draw(surface, 'Appuyer sur espace pour ', (920, 400))
        Stats.draw(surface, ' recommencer', (920, 430))
    elif state == States.gagne: #ici on montre ce qui est affiché aprés un jeu gagné
        Stats.draw(surface, 'Vous avez gagné!', (1000, 350))
        Stats.draw(surface, 'Appuyer sur espace pour  ', (920, 400))
        Stats.draw(surface, ' recommencer', (920, 430))
        

    grid.draw(surface)   #placement de chaque commande dans l'interface graphique
    grid.draw(surface) 
    Stats.draw(surface, 'Les vies réstantes', (950, 100))
    Stats.draw(surface, str(player.get_health()), (1020, 200))
    Stats.draw(surface, 'a pour afficher les mines', (920, 650))

    pygame.display.flip()