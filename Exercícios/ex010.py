#ex010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere : US$1,00=R$3,27
n1 = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar U${:.2f}!'.format(n1, n1/3.27))
#acertei 100% desse exercício sem consulta.
#abaixo resolução do professor:
real = float(input('Quanto dinheiro você tem na carteira'))
dolar = real / 3.27
print('Com R${} você pode comprar U${}'.format(real, dolar))