#ex021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
#Este exercicio não foi ensinado em aula, procurei no google e encontrei a resposta facilmente, achei desleal kkkk, teria sido mais legal "aprender" como fazer ao invés de achar a resposta pronta.
import playsound as sound
sound.playsound ('musica')
#abaixo resolução do professor:
import pygame
pygame.init()
pygame.mixer.music.load('')
pygame.mixer.music.play()
pygame.event.wait()