#ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa.
n1 = float(input('Qual é o comprimento do cateto oposto: '))
n2 = float(input('Qual é o comprimento do cateto adjacente: '))
print('A hipotenusa do triangulo vai medir: {:.2f}.'.format((n1**2+n2**2)**(1/2)))
#acertei esse desafio consultando a fórmula da hipotenusa, que é a raiz quadrada da soma dos quadrados dos catetos.
#Porém o interessante seria resolver este exercício utilizando a importação da biblioteca math pra por em pratica a aula 08
#abaixo resolução do professor:
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))