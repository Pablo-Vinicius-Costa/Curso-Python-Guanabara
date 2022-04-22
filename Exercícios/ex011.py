#ex011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Qual é a largura da parede: '))
altura = float(input('Qual é a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para poder pintar essa parede, você precisará de {}l de tinta.'.format(area/2))
#Acertei 100% deste exercício sem consultar, poderia ter gerado a multiplicação e resultado da 'area' direto no format, porém quis separar e gerar a váriável 'area' = largura * altura
#Abaixo resolução do professor:
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))