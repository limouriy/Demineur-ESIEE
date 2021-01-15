import pygame
from random import randint


pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 18) #pygame.font.SysFont sert à utiliser la police Cmic Sans MS en Taile 18 

class Cell:
    #ici on va utiliser la programmation orientée objet et on va initialiser toutes les variables qu'on va utiliser.
    def __init__(self, pos,mine_aleatoire):
        
        self.visible = False
        self.mine = mine_aleatoire
        self.montrer_mine = False
        self.size = 30
        self.couleur = (200,200,200)
        self.pos = pos
        self.label = False
        self.conteur_mine = 0
        self.font_couleur = (0, 0, 0)
        self.marked = False
        self.explosion = False

    def dessin(self, surface):
#pygame.draw.rect est une commande pour dessiner un réctangle ( on peut faire des modifications sur la couleur, surface etc )
#pygame.draw.circle dessine un cercle (ici on va l'utiliser pour marquer les lieux où se trouvent les mines)
        if self.visible:
            pygame.draw.rect(surface, self.couleur, (self.pos[0], self.pos[1], self.size, self.size))
        elif self.marked:
            pygame.draw.rect(surface, (150, 50, 50), (self.pos[0], self.pos[1], self.size, self.size))
        else:
            pygame.draw.rect(surface, (50,50,50), (self.pos[0], self.pos[1], self.size, self.size))
        if self.montrer_mine and self.mine:
            pygame.draw.circle(surface, (10,10,10), (self.pos[0]+15, self.pos[1]+15), 15)
        if self.explosion:
            pygame.draw.circle(surface, (255,10,10), (self.pos[0]+15, self.pos[1]+15), 15)

        if self.label:
            self.montrer_label(surface, self.conteur_mine, self.pos)

    def montrer_label(self, surface, label, pos):
        textsurface = myfont.render(label, False, self.font_couleur) #myfont.render pour créer l'objet texte
        surface.blit(textsurface, (pos[0]+10, pos[1]+4))


class Grid: #dans cette classe on va plutot s'appuyer sur le JEU et ses REGLES
#dans le fichier progdoc je vais detailler chaque fonction
    def __init__(self, player):
        self.player = player
        self.cells = []
        self.chercher_dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

        for y in range(30):
            self.cells.append([])
            for x in range(30):
                self.cells[y].append(Cell((x*30, y*30), self.mine_aleatoire()))

        self.lines =[]

        for y in range(1, 31, 1):
            temp = []
            temp.append((0, y * 30))
            temp.append((900, y * 30))
            self.lines.append(temp)

        for x in range(1, 31, 1):
            temp = []
            temp.append((x*30, 0))
            temp.append((x*30, 900))
            self.lines.append(temp)

    def mine_aleatoire(self):
        r = randint(0, 10)
        if r > 9:
            return True
        else:
            return False

    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.dessin(surface)
        for line in self.lines:
            pygame.draw.line(surface, (0, 125, 0), line[0], line[1])

    def respecter_limites(self, x, y): 
        return x >= 0 and x < 30 and y >= 0 and y < 30

    def chercher(self, x, y):
        if not self.respecter_limites(x, y):
            return

        cell = self.cells[y][x]

        if cell.visible:
            return

        if cell.mine:
            cell.montrer_mine = True
            cell.explosion = True
            self.player.sub_health()
            return

        cell.visible = True

        nombre_mines = self.nombre_de_mines(x, y)

        if nombre_mines > 0:
            cell.label = True
            cell.conteur_mine = str(nombre_mines)
            return

        for xx, yy in self.chercher_dirs:
            self.chercher(x+xx, y+yy)


    def nombre_de_mines(self, x, y):
        conteur = 0
        for xx, yy in self.chercher_dirs:
            if self.respecter_limites(x + xx, y + yy) and self.cells[y + yy][x + xx].mine:
                conteur += 1
        return conteur

    def clique(self, x, y):
        grid_x, grid_y = x//30, y//30
        self.chercher(grid_x, grid_y)

    def recharger(self):
        self.player.health = 5
        for row in self.cells:
            for cell in row:
                cell.visible = False
                cell.label = False
                cell.marked = False
                cell.montrer_mine = False
                cell.explosion = False
                cell.mine = self.mine_aleatoire()

    def check_if_win(self):
        if self.player.health < 1:
            return False
        for row in self.cells:
            for Cell in row:
                if not Cell.visible and not Cell.mine:
                    return False
        return True

    def montrer_mine(self):
        for row in self.cells:
            for cell in row:
                if not cell.montrer_mine:
                    cell.montrer_mine = True
                else:
                    cell.montrer_mine = False


    def marquer_mine(self, x, y):
        self.cells[y][x].marked = True