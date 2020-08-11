#21-Tocando musica
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

