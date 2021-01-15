<u>***#groupe : Limouri Youssef***</u>

<u>***#projet : Démineur***</u>



Dans ce fichier je vais essayer de montrer l'**architecture globale de mon code** :



Globalement, le code est réparti sur 3 grandes parties,   la première partie **main.py** ( qu'il faut exécutée )  où j'ai utilisé la classe <u>States</u> , la deuxième partie **board.py** , j'ai utilisé les deux classes <u>Cell</u> et <u>Grid</u> , puis enfin une dernière petite partie **player.py**  où j'ai exploité les deux classes <u>Player</u> et <u>Stats</u>.



Dans ce fichier je vais détailler le rôle de chaque fonction importante utilisée   :

​                                            ***<u>PARTIE MAIN :</u>***

​               <u>**Class States**:</u>

​      Dans cette partie, j'ai utilisé une boucle While qui prend "**parcourir**" comme paramètre et fait une énumération des cas possible par exemple le cas d'une/un victoire/échec etc,  et mis en œuvre l'affichage des consignes sur l'interface graphique et leurs positionnement par exemple si le nombre de vies devient nul alors on affiche 'Le jeu est terminé! ' dans la position (970,300).



​                                             ***<u>PARTIE BOARD:</u>***

​                 <u>**Class Cell :**</u>

​     Dans cette partie où on fera appel à la programmation orientée objet , d'abord on va commencer par initialiser plusieurs variables qui seront utiles dans la suite :

--     La fonction <u>**draw**</u> avec "**surface**" comme paramètre qui sert à dessiner les petits carreaux qui représentent les cases et les cercles qui représentent les mines.

--     La fonction <u>**montrer_label**</u> qui utilise la commande "render" qui sert à créer l'objet texte dans la surface puis la commande "blit" qui donne la position du texte.



​                 <u>**Class Grid :**</u>

--     La fonction <u>**mine_aleatoire**</u>  utilise randint qu'on a déjà importé de random est qui donne un nombre aléatoire entre start et stop ---> randint([start],[stop])

--     La fonction **<u>respecter_limites</u>** qui prend "**x et y**" comme paramètres sert  à ne pas dépasser les bornes de l'interface (ici on doit rester entre 0 et 30 dans les deux sens x et y ) 

--     La fonction **<u>chercher</u>** montre sur quoi on tombe en cliquant sur une case (par exemple si une case s'explose cela veut dire qu'il y a une mine dedans dans on fait une substruction 5-1=4 vies restantes ) sinon on montre le nombre qui est dans la case (cell.visible)

--     Les fonctions **<u>nombre_de_mines</u>** et **<u>clique</u>** prennent " **x et y**"comme paramètres aussi complètent le rôle de la fonction chercher. 

--     La fonction **<u>check_if_win</u>** , dans cette fonction on va vérifier si on a gagné ou pas   ( si le nombre de vies <1 donc =0 cela veut dire qu'on a perdu sinon on a gagné ) 

--     Les fonctions **<u>montrer_mine</u>** et **<u>marquer_mine</u>**  montrent et marquent les mines dans une position  (x,y).



​                                                 ***<u>PARTIE PLAYER :</u>***

​                    <u>**Class Player:**</u>



​     Dans cette classe il y aura 3 fonctions qui vont servir à donner au joueur au début 5 vies, s'il se trompe en touchant une case minée alors il perd une vie chaque fois  sinon il perd aucune.



​                     <u>**Class Stats :**</u>

​     

​      Dans cette classe on fera appel aux mêmes commandes utilisées dans la fonction **montrer_label** dans la partie **<u>board.py</u>** 