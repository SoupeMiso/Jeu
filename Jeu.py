"""Jeu qui n'a pas encore de nom"""
import pygame,math,os,random
from pygame.locals import *
pygame.init()

#Ouverture de la fenêtre et compagnie
fenetre = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jeu qui n'a pas de nom")

font = pygame.font.Font(None, 30)
#bonjour a toi jeune poire
mot1 = font.render(("Bonjour "),1,(255,255,255))
mot2 = font.render(("à "),1,(255,255,255))
mot3 = font.render(("toi "),1,(255,255,255))
mot4 = font.render(("jeune "),1,(255,255,255))
mot5 = font.render(("poire "),1,(255,255,255))
continuer = 1
x = 50
y = 50
mot = 1

while continuer==1:
    pygame.time.Clock().tick(8)
    if mot == 1:
        fenetre.blit(mot1, (x,y))
        x+=80
    if mot == 2:
        fenetre.blit(mot2, (x,y))
        x+=15
    if mot == 3:
        fenetre.blit(mot3, (x,y))
        x+=30
    if mot == 4:
        fenetre.blit(mot4, (x,y))
        x+=60
    if mot == 5:
        fenetre.blit(mot5, (x,y))
        x+=60
        continuer = 0
    mot+=1
    pygame.display.flip()
