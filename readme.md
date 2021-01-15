<u>***#groupe : Limouri Youssef***</u>

<u>***#Projet : démineur.***</u>





-- **<u>MISE EN PLACE DES APPS  UTILISÉES</u>** :



1) D'abord on va commencer par télécharger l'interface graphique **<u>Pygame</u>** par une simple commande dans le Terminale (commande : **<u>pip install pygame</u>** ) 



(REMARQUE : pour vérifier que pygame a bien été télécharger en va utiliser la commande  "import pygame"

si la réponse est "no module named 'pygame'" alors l'interface n'a pas été bien téléchargée sinon c'est BON )



2) Pour le 'code editor' j'utiliserai **<u>Visual  Studio Code</u>** comme on avait l'habitude de faire en école.



3) Ouvrir les 3 fichiers **<u>board.py</u>** , **<u>player.py</u>** et **<u>main.py</u>** dans <u>Visual Studio Code</u>.



4) Comme chaque interface graphique, on aura besoin de plusieurs commandes spécifiques.

pour cela j'introduirai également un fichier **<u>Pycommandes.md</u>** contenant plusieurs (les plus importantes bien évidemment ) commandes qui constituent les bases du fonctionnement de mon Projet. 



-- **<u>RÈGLES DU JEU</u>** :

Généralement, le but de ce jeu est de trouver toutes les grilles vides sans faire exploser les mines. 

Le jeu donne aléatoirement des nombres : Chaque nombre désigne le nombre de mines dans les 8 cases qui l'encercle. 

exemple : 

Si dans une case on trouve le nombre 3 --> alors automatiquement on doit trouver exactement 3 mines dans les 8 cases qui l'entoure.



Le joueur à 5 vies ---> Donc 5 fois à avoir échouer à trouver la BONNE = VIDE case.

​          J'ai ajouté l'option de montrer les mines aussi ,pour l'enlever on efface la ligne suivante : Stats.draw(surface, 'a pour afficher les mines', (920, 650))) 

​          Pour afficher une mine, on appuie sur le bouton droit de la souris. 

​          Pour afficher le nombre existant (Dans le cas où on est sur qu'il y a pas de mine dans la case!!!!! ) dans une case on appuie sur le bouton gauche de la souris.  





