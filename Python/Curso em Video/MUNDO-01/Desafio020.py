### o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome
### dos quatro alunos e mostre a ordem sorteada

import random

# Lista de nomes
nome1 = str(input('digite  o nome do Aluno 1: '))
nome2 = str(input('digite  o nome do Aluno 2: '))
nome3 = str(input('digite  o nome do Aluno 3: '))
nome4 = str(input('digite  o nome do Aluno 4: '))
alunos = [nome1, nome2, nome3, nome4]
print(random.choices(alunos))
random.shuffle(alunos)
print(alunos)
