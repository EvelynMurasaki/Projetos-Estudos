# Faça um programa que leia um numero inteiro e mostre na tela o seu
# sucessor e seu antecessor

valor = int(input('Digite um numero inteiro:'))
antes = valor - 1
depois = valor + 1

print('o numero anterior de {} é {} e o numero posterior a ele é {}'.format(valor, antes, depois))
#print('o numero anterior de {} é {} e o numero posterior a ele é {}'.format(valor, (valor-1), (valor+1))