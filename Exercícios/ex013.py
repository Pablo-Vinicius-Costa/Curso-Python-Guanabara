#ex013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passará a receber R${:.2f}.'.format(salario, salario*115/100))
#acertei esse exercicio sem consulta e com facilidade por se tratar de uma pequena variação do exercício anterior.
#Abaixo a resolução do professor:
salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novo))