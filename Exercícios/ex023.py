#ex023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
n1 = int(input('Informe um número: '))
n2 = str(n1)
print('Analisando o número {}'.format(n1))
print('Unidade: {}'.format(n2[3]))
print('Dezena: {}'.format(n2[2]))
print('Centeza: {}'.format(n2[1]))
print('Milhar: {}'.format(n2[0]))
#Acertei este desafio parcialmente, pois caso digite algum numero com menos de 4 digitos meu programa da erro.
#abaixo resolução do professor:
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(n1))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centeza: {}'.format(c))
print('Milhar: {}'.format(m))