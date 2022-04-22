#ex024 - Crie um programa que leia o nome de sua cidade e diga se ela começa ou não com o nome "Santo".
cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cidade[:5] == 'Santo')
#Acertei parcialmente este desafio, nao utilizei a função upper ou lower para contorna a escrita do usuário,
#só percebi que meu programa não estava completo quando vi a resolução do professor.
#abaixo resolução do professor:
cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')