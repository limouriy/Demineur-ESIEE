<u>***#Groupe : Limouri Youssef***</u>    

<u>***#Projet : Démineur***</u>         



​                         

***REMARQUE IMPORTANTE*** : <u>J'ai trouvé ce fichier sur Internet, je l'ai complètement modifié pour qu'il soit utile pour mon Jeu . J'ai mis en Gras toutes les commandes que j'ai utilisées ( Ces commandes sont uniques  à l'interface graphique Pygame ) . J'ai supprimé toutes les commandes qui ne touchent pas à mon projet pour que ce Fichier soit le plus concentré et efficace que possible.</u> (j'ai passé de 2400 mots à 960)











​                                    <u>***Bases de l'utilisation de Pygame***</u>





Ce fichier vous présente quelques commandes de Pygame, permettant tout de même
de réaliser de nombreux programmes dont mon projet "Démineur".

***<u>0) Remarques préliminaires</u>*** :

a) Pour interagir avec pygame on utilise des évènements qui peuvent être un clic de
la souris, un appui sur une touche etc….Ces évènements sont stockées dans une file
qui s'appelle pygame.event. Les événements sont traités dans leur ordre
chronologique. On peut avoir le type de l'évènement grâce à la commande
event.type.  Avec des instructions conditionnelles, on peut gérer les actions
correspondant aux différents évènements.

b)Les positions d'un objet sont toujours calculées à partir du coin en haut à gauche
du contenant (c’est-à-dire de l'écran pour la fenêtre, de la fenêtre pour les objets qui
sont tracés dessus…etc…) et on donne toujours d'abord l'abscisse (de 0 à gauche à
la largeur de la fenêtre à droite) puis l'ordonnée (de 0 en haut jusqu'à la hauteur de la
fenêtre en bas : l'axe des ordonnées va donc vers le bas..).

**<u>1) Création d'une fenêtre :</u>**

Voici le schéma d’un programme créant une fenêtre Pygame :

***import pygame***  #importation de pygame
***import os***
***pygame.init()***  #on lance pygame
***os.environ['SDL_VIDEO_WINDOW_POS']="400,600"*** #pour positionner la fenêtre sur l'écran à la position (400,600).
#création d'une fenêtre
***fenetre=pygame.display.set_mode((640,480))***#fenêtre de taille 640*480

#boucle perpétuelle qui permet de garder la fenêtre ouverte
***while continuer:***
***for event in pygame.event.get():***
#pygame prend le premier évènement de la file
***if event.type==QUIT:***  #l'évènement QUIT correspond au clic sur la croix
continuer=0  #permet de quitter la boucle

<u>Commandes additionnelles</u> :

• mettre un titre à la fenêtre :
***pygame.display.set_caption("Mon_titre")***  #ici Mon_titre = Démineur
• rafraîchir l'écran : indispensable après toute modification:
***pygame.display.flip()***
Mise en oeuvre : Créer une fenêtre de taille 300*200 coloriée en bleu

**<u>2) Evènements .</u>**

Exemple :
On reprend le programme du début et on insère après le bloc "if event.type==QUIT",
d'autres blocs, par exemple :
***if event.type==KEYDOWN:*** #appui sur une touche
***if event.key==K_UP***:  #la touché est la flèche vers le haut
• ***event.type==QUIT*** (c'est l'une des "constantes importées de pygame .locals)
c'est le fait d'appuyer sur la croix : vous pouvez décider d'associer ceci à la
fermeture de la fenêtre (c'est ce qui est fait en général) ou autre chose !
• ***event.type==KEYDOWN***
correspond à l'enfoncement d'une touche (il y a aussi KEYUP)
On peut alors récupérer la touche appuyée avec la commande :
event.key qui peut prendre différentes valeurs.



#commander la sourie et le Clavier avec :

*** K_a pour le a (et pareil pour le reste de l'alphabet)***
*** K_0 pour les chiffres en haut du clavier***
*** K_F1 pour la touche F1***
*** K_SPACE pour la touche espace***
*** K_RETURN pour la touche ENTER***
*** K_ESCAPE pour la touche Echap***
*** K_UP pour la flèche vers le haut (DOWN, LEFT, RIGHT)***
*** K_KP0 pour le 0 du pavé numérique***

Ou encore :

• ***event.type==MOUSEBUTTONDOWN***  #quand on clique avec la souris . Pour récupérer les coordonnées x et y de la position de la souris on écrit (x,y)=event.pos

**<u>3) Les mouvements.</u>**

Il est recommandé d'utiliser des rectangles qui contiennent les objets, ce qui permet
de les déplacer facilement et de mieux gérer l'affichage, les effets de bord et les
collisions.
• pour récupérer le rectangle d'un objet appelé objet :
***objet_rect=objet.get_rect()***
#objet_rect vaut alors (x,y,largeur,hauteur) où (x,y) est la position de l’objet et largeur et hauteur sont les dimensions du rectangle qui entoure l’image.
• pour créer un rectangle :
***mon_rect=pygame.Rect(x,y,largeur, hauteur)***  #où x,y correspond à la position
du rectangle
fenetre.blit(objet,mon_rect) et pour le fond cela dépend des situations (voir
l'exemple qui suit) et ne pas oublier de rafraîchir la fenêtre ***fenetre.display.flip()***

**<u>4) Les textes</u>**

Voici comment afficher une chaîne.
• chaine="ma chaine sur une seule ligne" (penser à la méthode format pour
afficher une chaîne contenant des données variables, par exemple le nom du
joueur ou le score)
• ***font=pygame.font.SysFont("broadway",24,bold=False,italic=False)***   #pour choisir
la police broadway , en taille 24, pas de gras, pas d'italique.
• ***text=font.render(chaine,1,(R,G,B))***  #pour créer l'objet texte
• ***fenetre.blit(text,(30,30)) où (30,30)***  #correspond à la position du texte
• ***fenetre.display.flip()***  #pour rafraîchir l'affichage

**<u>5) Les dessins</u>**

On peut dessiner des formes dans pygame :
• un rectangle :

 ***mon_rectangle=pygame.draw.rect(surface,color,rect,épaisseur)***
avec surface est la surface sur laquelle on veut dessiner le rectangle (la
fenêtre ou autre chose), color c'est un triplet (R,G,B), rect correspond à la
position : ce peut être un pygame.Rect ou (positionx, positiony, largeur,
hauteur) ,épaisseur est l'épaisseur du trait (0 donne un rectangle plein)
• un cercle :
***mon_cercle=pygame.draw.circle(surface,color,pos_centre,rayon,épaisseur)*** #pos_centre est du type (x,y)
On peut créer des surfaces (par exemple pour avoir deux parties dans une fenêtre) :
ma_surface=pygame.Surface((34,34)) crée un rectangle noir de taille 34*34
On peut le remplir entièrement ou partiellement :
**surf.fill((R,G,B)*** le remplira entièrement
Ceci s'applique aussi au remplissage de la fenêtre.



