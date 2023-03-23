#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

valor =int(input('Qual é o numero que deseja calcular?'))

dobro = valor*2
triplo = valor*3
raiz = valor**(1/2)

print('O dobro do valor {} é: {} \no triplo é: {} \ne a raiz é: {:.2f}'.format(valor, dobro, triplo, raiz))