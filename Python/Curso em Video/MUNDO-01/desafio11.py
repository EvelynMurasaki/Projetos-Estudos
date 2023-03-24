#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta
#necessaria par pinta -la sabendo que cada litro de tinta pinta uma area de 2m²
#EXEMPLO DO PROFESSOR
largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
print ('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar a sua parede, voce vai precisar de {}L de tinta.'.format(tinta))