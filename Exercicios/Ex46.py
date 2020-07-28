# Contagem regressiva
import pygame
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print("\033[30m CONTAGEM FINALIZADA")
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex46.mp3')
pygame.mixer.music.play()
pygame.event.wait()




