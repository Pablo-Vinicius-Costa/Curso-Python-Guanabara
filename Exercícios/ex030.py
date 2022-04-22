#ex030 - Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou IMPAR.
n1 = int(input('Me diga um número qualquer: '))
n2 = n1 % 2
if n2 == 0:
    print('O número {} é PAR!'.format(n1))
else:
    print('O número {} é ÍMPAR!'.format(n1))
#Acertei este desafio consultado a aula de operadores aritméticos e utilizando o "%" que em python significa resto da divisão.
#todo numero par quando dividido por 2 o resultado do resto da divisião SEMPRE será 0.

#Abaixo resolução do professor:

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))