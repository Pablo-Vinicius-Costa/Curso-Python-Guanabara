#ex018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n1 = float(input('Digite o ângulo que você deseja: '))
n2 = math.sin(n1)
n3 = math.cos(n1)
n4 = math.tan(n1)
print ('O ângulo de {} tem o seno de {:.2f} O ângulo de {} tem o cosseno de {:.2f} O ângulo de {} tem a tangente de {:.2f}'.format(n1, n2, n1, n3,n1 , n4))
#usei o google tradutor pra tentar achar as funcionalidades seno, cosseno e tangente dentro da biblioteca math porém adicionei as funcionalidades erradas kkk.
#obs 2, parece que as funcionalidades importadas estavam corretas porém precisava realizar a conversão de graus para radianos antes.
#abaixo a resolução do professor:
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f} .'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f} .'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f} .'.format(angulo, tangente))
#OU
from math import sin, cos, tan, radians
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f} .'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f} .'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f} .'.format(angulo, tangente))