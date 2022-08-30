'''
Faça um programa em python que abra e reproduza o áudio de um
arquivo MP3.
'''

import pygame

pygame.init()
pygame.mixer.music.load('musica1.mp3')
pygame.mixer.music.play()

print('Tocando musica ======')
input()
pygame.event.wait()
print('Música finalizada ======')
