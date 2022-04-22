#  Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele :
a = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está somente em letras maiúsculas?', a.isupper())
print('Está somente em letras minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
#Nota-Acertei parcialmente este exercício, pois não coloquei todas essas váriaveis.