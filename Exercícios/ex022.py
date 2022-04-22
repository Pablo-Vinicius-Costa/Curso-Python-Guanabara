#ex022 - Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas,
#o nome com todas minúsculas, quantas letras ao tdo (sem considerar espaços), e quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras !'.format(len(nome)))
print('Seu primeiro nome tem {} letras !'.format(nome.find(' ')))
#acertei esse exercicio parcialmente,não soube inserir as funcionalidades ".strip e -nome.counter(' ') para contabilizar corretamente a quantidade de digitos presente no nome inserido.
#Abaixo resolução do professor:
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras !'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras !'.format(separa[0], len(separa[0])))