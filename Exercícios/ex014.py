#ex014 - Escreva um programa que converta uma temperatura digitada em Cº e converta para F°.
c = float(input('Informe a temperatura em ºC: '))
print('A temperatura de {}ºC corresponde a {}F°.'.format(c, c*1.8+32))
#Acertei 100% desse desafio, consultei na internet qual era a fórmula matemática para conversão de °C para °F e apliquei a fórmula em meu programa.
#Abaixo a resolução do professor:
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}F°.'.format(c, f))
#Fórmula que eu utilizei: °C*1.8+32, fórmula que o professor utilizou: 9*°C/5+32 .