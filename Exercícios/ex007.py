#ex007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média:
a = int(input('Digite a primeira nota do aluno: '))
b = int(input('Digita a segunda nota do aluno: '))
print('A média entre {} e {} é igual a {}!'.format(a, b, (a+b)/2))
#Acertei parcialmente esse exercício, usei o comando int ao invés do float, desta forma meu programa só aceita números inteiros, o comando float permite preencher com notas fracionadas.
#Abaixo resolução do professor:
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print(' A média entre {:.1f} e {:.1f} é igual a {:.1f}!'.format(n1, n2, m))