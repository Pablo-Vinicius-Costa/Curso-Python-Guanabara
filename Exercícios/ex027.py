#ex027 - Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome separadamente.
nome = str(input('Digite o seu nome: ')).strip()
print('Muito prazer em ti conhecer {}!'.format(nome))
print('Seu primeiro nome é {}'.format(nome.split()[0]))
#Consegui realizar apenas metade do exercicio,nao sei como mostrar em python o último nome considerando nomes de diferentes tamanhos.
#abaixo resolução do professor:
n = str(input('Digite seu nome: '))
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
#obs1 - Não entendi esse '-1', nao foi explicado o porque dele.
#obs2 - procurei os comentarios da aula e aprendi o detalhe que não foi explicado em aula, o -1 mostra o último nome da lista, -2 o penúltimo e assim sucetivamente.
#também poderia ter sido feito sem o 'len' da forma abaixo
print('E seu último nome é {}'.format(nome[-1]))