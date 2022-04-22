#ex035 - Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou nao formar um trinagulo.
print('-='*15)
print('Analisador de Triangulos')
print('-='*15)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n2 < n1 + n2:
    print('Os segmentos acima PORDEM FORMAR Triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo!')
#Acertei este desafio, consultei o google e vi que a regra do triângulo é que 1 lado seja menor do que a soma dos outros 2 lados.
#Abaixo resolução do professor:
print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PORDEM FORMAR Triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo!')