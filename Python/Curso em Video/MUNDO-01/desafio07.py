#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
nota1 = float(input('Qual o valor da primeira nota?'))
nota2 = float\
    (input('Qual valor da segunda nota?'))

somanota = nota1+nota2
somamedia = somanota/2
notafinal = (nota1+nota2)/2 #exemplo extra de como tem como resolver em uma unica linha
print('A soma da sua nota é: {}, portanto sua média é {}'.format(somanota, somamedia))
print('A nota final é: {}'.format(notafinal))
