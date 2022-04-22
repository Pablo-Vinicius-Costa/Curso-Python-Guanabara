#ex026 - Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece letra "A",
#em que posição ele aparece a primeira vez, em que posição ele aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase!'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição: {}'.format(frase.upper().find('A')+1))
print('A última letra A apareceu na posição: {}'.format(frase.upper().rfind('A')+1))
#acertei parcialmente este exercicio, pois o python conta a posição do carácterer apartir de 0, e ao consultar a
#resolução, identifiquei que poderia adicionar +1 dentro do format e obter a contagem do python como
#se estivesse iniciando apartir de 1 ao invés de apartir de 0.
#abaixo resolução do professor:
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))