#ALUGUEL DE CARROS
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#exemplo feito pela Evelyn

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km rodados? '))
pagoD = dias * 60
pagoK = km * 0.15
pagafinal = pagoD + pagoK
print('O total de dias a pagar é {:.2f} adicionando os Km {:.2f} rodado o valor final vai ser {:.2f}'.format(pagoD,pagoK, pagafinal))

#exemplo feito pelo professor
Dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos KM rodado? '))
pago = (dias * 60) + (Km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))