#Crie um programa que quanto dinehiro uma pessoa tem na carteira e mostre quantos ela pode comprar
#considere o valor do dolar 1 = 3,27k

#EXEMPLO REALIZADO PELO PROFESSOR

real = float(input('Quantos de dinheiro voce tem na carteira?? R$ '))
dolar = real/5.36
print('Com R${:.2f} voce pode comprar U$${:.2f}'.format(real, dolar))
 #fazer agr com euro e outras moedas desafio extra