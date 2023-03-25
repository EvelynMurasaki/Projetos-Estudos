#### Desafio 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
#### escrevendo o nome do escolhido
import random

# Lista de nomes
nome1 = str(input('digite  o nome do Aluno 1: '))
nome2 = str(input('digite  o nome do Aluno 2: '))
nome3 = str(input('digite  o nome do Aluno 3: '))
nome4 = str(input('digite  o nome do Aluno 4: '))
alunos = [nome1, nome2, nome3, nome4]
escolhido = random.choice(alunos)
print(random.choice(alunos))
print('O Aluno escolhido foi {}'.format(escolhido))