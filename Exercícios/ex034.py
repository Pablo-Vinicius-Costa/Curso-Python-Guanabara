#ex034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$ 1.250,00, cacule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n1 = float(input('Qual é o salário do funcionário? R$'))
if n1 > 1250:
    n2 = 10 / 100
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(n1, n1 + (n1 * n2)))
if n1 < 1250:
    n2 = 15 / 100
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(n1, n1 + (n1 * n2)))
#Acertei este desafio, consultei exercicios antigos pra relembrar como eu acho e utilizo um percentual em python...
#Abaixo resolução do professor:
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <=1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))