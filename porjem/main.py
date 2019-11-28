import pygame
import os

kelimeler = ["kapı","mice","duvar","skull","bayrak","lav","cimen","su"]
aksiyonlar = ["sensin","galibiyet","yüzer","engel","ölüm"]

pygame.init()

#ekranı oluşturduk
ekran = pygame.display.set_mode((1000,600))

#açılır pencere ismi ve ikonu
pygame.display.set_caption("Aslında Sensin")
ikon = pygame.image.load('icons-hamster.png')
pygame.display.set_icon(ikon)

#player
playerimg = pygame.image.load('player.png')
playerx = 480
playery = 480
xchange = 0


def player(x,y):
    ekran.blit(playerimg,(x,y))

#açılır pencere loop
calisirdurum = True
while calisirdurum:
    ekran.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisirdurum = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -2
            if event.key == pygame.K_RIGHT:
                xchange = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0





    playerx += xchange
    if playerx <=0:
        playerx=0
    elif playerx >=936:
        playerx=936
    player(playerx,playery)
    pygame.display.update()
