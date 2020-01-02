"""
Author : Camille Clarret
Date : 12/24/2019
Goal :  help MacGuiver to find the 3 items and to find the exit
Input : key events
Output : ???
"""

#Import
from Player import *
from Items import *
from Map import *
from data import *
from pygame.locals import *

#Main Code

#Lancer la fonction de création du jeu
#init_game()

#Afficher un truc de départ + jeu

#Comment faire évoluer la position
#move(event) >>> cette partie est à gérer avec player <<<

#Comment déterminer si gagné ou perdu
#Si position = "F" et items = 3 alors ok sinon si position = "F" et items < 3 alors perdu

#Relancer le jeu ?

#quit the window
dead = False
while(dead == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True