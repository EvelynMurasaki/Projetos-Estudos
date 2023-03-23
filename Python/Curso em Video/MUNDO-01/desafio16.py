#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#EXEMPLO - digite um numero 6.127 o numero 6.127 tem a parte inteira 6
#01
num = float(input('Digite um numero real: '))
print(int(num))
#02
try:
    num = float(input('Digite um numero real: '))
    print(int(num))
except:
    print('fail baka')

#exemplo feito pelo professor
import math
num1 = float(input('Digite um numero: '))
print('O numero digitado foi {} e sua porção inteira é {}. '.format(num1, math.trunc(num1)))
