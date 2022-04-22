#ex005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
n1 = int(input('Digite um número: '))
n2 = n1 + 1
n3 = n1 - 1
print('Analisando o valor {}, o seu sucessor é {}, e seu antecessor é {}!'.format(n1, n2, n3))
#Acertei este exercício .
#Abaixo resolução do professor:
n = int(input('Digite um número: '))
print('Analisando o valor {}, o seu sucessor é {}, e seu antecessor é {}!'.format(n1, n1+1, n1-1))