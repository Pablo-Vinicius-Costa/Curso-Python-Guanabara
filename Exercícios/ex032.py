#ex032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
import calendar
from calendar import isleap
ano = int(input('Que ano quer analisar? '))
anobi = calendar.isleap(ano)
if anobi is True:
    print('O ano de {} é bissexto !'.format(ano))
else:
    print('O ano de {} não é bissexto !'.format(ano))
#Acertei este desafio consultado o google e aprendendo a importar a função isleap da biblioteca calendar
#Abaixo resoluçaõ do professor:

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))