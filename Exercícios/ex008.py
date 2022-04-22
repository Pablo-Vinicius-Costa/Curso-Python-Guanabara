#ex008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:
#extra - adicione a medida em km,hm, dam, dm,cm e mm.
n1 = float(input('Uma distância em metros: '))
print('A medidas de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n1, n1/1000, n1/100, n1/10, n1*10, n1*100, n1*1000))
#Acertei 100% deste exercício sem consulta.
#Abaixo resolução do professor:
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))