#Escreva um programa que leia um valor em metros e o exiba convertido e, centimetros e milimetros

metro = float(input('Quantos metros deseja calcular?'))
cm = metro * 100
mm = metro * 1000

print('O valor {}m convertido para centimetros é: {:.0f}cm e milimetros é {:.0f}mm'.format(metro, cm, mm))
