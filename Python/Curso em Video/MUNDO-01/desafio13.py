#Faça um algotimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

#RESOLUÇÂO FEITA POR EVELYN
salario = float(input('Qual é salario atual do funcionario? R$:'))
aumento = salario * 15 / 100 #aqui so estou fazendo uma conta oculta nao preciso chamar no format
salarioFinal = salario + aumento
print('O valor do salario de R${:.2f} foi para {:.2f} devido ao aumento de 15%.'.format(salario,salarioFinal))

#EXEMPLO PROFESSOR

salário = float(input('Qual é o salario do funcionario: R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))

#exercicio extra fazer uma simulação de compra a vista e a prazo mostrando na tela o desconto a vista e o aumento se for parcelado