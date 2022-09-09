'''
Faça um programa em python que abra e reproduza o áudio de um
arquivo MP3.
'''

import pygame
import color

pygame.init()
pygame.mixer.music.load('musica1.mp3')
pygame.mixer.music.play()

print('{} Tocando musica ======> {}'.format(color.cor['azul'],color.cor['limpa']))
input()
pygame.event.wait()
print('{} Música finalizada ====== {}'.format(color.cor['vermelho'],color.cor['limpa']))
