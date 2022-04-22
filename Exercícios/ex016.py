#ex016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
n1 = float(input('Digite um número: '))
n2 = trunc(n1)
print('O valor digitado foi de {} e a sua porção inteira é {}!'.format(n1, n2))
#ou
print('O valor digitado foi de {} e a sua porção inteira é {}!'.format(n1, trunc(n1)))
#Acertei 100% desse desafio com consulta do material teórico da aula 08.
#Abaixo resolução do professor:
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi de {} e a sua porção inteira é {}!'.format(num, math.trunc(num)))
#ou sem utilizar a biblioteca math seria da forma abaixo, mais o interessante é por em prática a importação da biblioteca.
num = float(input('Digite um número: '))
print('O valor digitado foi de {} e a sua porção inteira é {}!'.format(num, int(num)))