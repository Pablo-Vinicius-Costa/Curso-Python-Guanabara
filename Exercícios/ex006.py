#ex006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadradada:
n1 = int(input('Digite um número: '))
n2 = n1*2
n3 = n1*3
n4 = n1**(1/2)
print('Analisando o número {}, o dobro é {}, o triplo é {}, e a raiz quadrada é {:.3f}!'.format(n1, n2,n3,n4))
print('Analisando o número {}, \no dobro é {}, \no triplo é {}, \ne a raiz quadrada é {:.3f}!'.format(n1,n1*2, n1*3, n1**(1/2)))
#Acertei 100% deste exercício, com uma pequena consulta do exercício anterior para por em pratica a forma mais eficiente de gerar o programa.