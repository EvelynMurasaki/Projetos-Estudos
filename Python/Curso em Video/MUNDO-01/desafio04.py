#Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possiveis (exemplo.. usar type e isnumerico, isalpha)

valor = input('Escreva algo para descobrir seu tipo:')
print('o seu tipo é: ', type(valor))
print('é alfa numerico?',valor.isalnum())
print('é alfabetico?',valor.isalpha())
print(valor.isascii())
print(valor.isdecimal())
print(valor.isdigit())
print(valor.isidentifier())
print('é minuscula?', valor.islower())
print('é um numero?', valor.isnumeric())
print(valor.isprintable())
print(valor.isspace())
print('é capitalizada?',valor.istitle())#nomes que tem letras maisculas e minusculas junto
print('é maiuscula?', valor.isupper())

# a variavel valor é nosso objeto por isso chamamos ele pra identificar o que é