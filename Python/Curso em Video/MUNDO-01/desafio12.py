#Faça um algoritmo que leia o preço de um produto e mostre seu preço com 5% de desconto.
#RESOLUÇÂO FEITA POR EVELYN

produto = float(input('Qual é o preço do produto? R$'))
desconto = produto * 5 / 100
resultado = produto - desconto
print('O valor do produto de R${} foi para {} devido ao desconto de 5%.'.format(produto,resultado))



#EXEMPLO DO PROFESSOR
preco = float(input('Qual é o preço do produto? R$:'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))
