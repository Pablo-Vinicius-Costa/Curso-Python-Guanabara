#ex031 - Desenolva um programa que pergunte a distancia de uma viagem em km.Calcule o preço da passagem,
# cobrando R$0,50 por km
# para viagens de até 200km e R$0,45 para viagens mais longas.
n1 = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(n1))
if n1 < 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(n1 * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(n1 * 0.45))
#Acertei este desafio !
#Abaixo resolução do professor :
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))