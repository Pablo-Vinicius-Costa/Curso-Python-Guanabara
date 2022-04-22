#ex015 - Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
aluguel = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
a = (aluguel * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}!'.format(a))
#ou
print('O total a pagar é de R${:.2f}!'.format(aluguel*60+km*0.15))
#Acertei 100% do exercício .
#Abaixo resolução do professor:
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}.'.format(pago))