#ex019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
print('O aluno escolhido foi {}!'.format(random.random(n1, n2, n3, n4)))
#Errei este exercício, não sabia qual funcionalidade da biblioteca random utilizar, apos assistira explicação do professor consegui executar.
#abaixo resolução do professor:
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}!'.format(escolhido))
