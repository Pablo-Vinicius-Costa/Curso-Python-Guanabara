#ex012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Qual é o preço do produto? R$'))
valor2 = valor * 95
valor3 = valor2 / 100
print('O produto que custa R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, valor3))
#ou
print('O produto que custa R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, valor*95/100))
#Acertei o exercício consultando minhas anotações da aula 7 e constatei que o sinal % não representa percentual dentro do python e sim módulo ou resto da divisão, ou seja não posso executar valor - 5%, neste caso usei como parâmetro regra de 3 para chegar no resultado esperado.
#abaixo resolução do professor:
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))