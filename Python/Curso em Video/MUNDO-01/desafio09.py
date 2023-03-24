#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
 #PRIMEIRA FORMA DE REALIZAR O CALCULO
numero = int(input('Olá, digite um numero inteiro para fazer a tabuada:'))
num0 = numero * 0
num1 = numero * 1
num2 = numero * 2
num3 = numero * 3
num4 = numero * 4
num5 = numero * 5
num6 = numero * 6
num7 = numero * 7
num8 = numero * 8
num9 = numero * 9
num10 = numero * 10

print('O valor da tabuada para ser calculado é : {}'.format(numero))
print('=' * 12)# questao de estetica, é pra deixar com traços no codigo
print('{} x 0 = {}'.format(numero, num0))
print('{} x 1 = {}'.format(numero, num1))
print('{} x 2 = {}'.format(numero, num2))
print('{} x 3 = {}'.format(numero, num3))
print('{} x 4 = {}'.format(numero, num4))
print('{} x 5 = {}'.format(numero, num5))
print('{} x 6 = {}'.format(numero, num6))
print('{} x 7 = {}'.format(numero, num7))
print('{} x 8 = {}'.format(numero, num8))
print('{} x 9 = {}'.format(numero, num9))
print('{} x 10 = {}'.format(numero, num10))
print('=' * 12)
# SEGUNDA FORMA DE REALIZAR O CALCULO feita pelo professor
print('=' * 12)
num = int(input('Digite um numero: '))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('=' * 12)
