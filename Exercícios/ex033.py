#ex033 - Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
val3 = int(input('Digite o terceiro valor: '))
if val1<val2 and val1<val3:
    print('O menor valor digitado foi {}.'.format(val1))
if val2<val1 and val2<val3:
    print('O menor valor digitado foi {}.'.format(val2))
if val3<val1 and val3<val2:
    print('O menor valor digitado foi {}.'.format(val3))
if val1>val2 and val1>val3:
    print('O maior valor digitado foi {}.'.format(val1))
if val2>val1 and val2>val3:
    print('O maior valor digitado foi {}.'.format(val2))
if val3>val1 and val3>val2:
    print('O maior valor digitado foi {}.'.format(val3))
#Acertei este desafio, mais acredito que tenha uma forma mais eficaz de realizar o mesmo, ficou um programa grandão pra algo simples...
#Abaixo resolução do professor :
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}.'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}.'.format(maior))