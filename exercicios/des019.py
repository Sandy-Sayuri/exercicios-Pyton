#um professor quer sortear 4 alunos pra apagar o quadro.Faça um programa que ajude ele ,lendo o nome deles e escrevendo o nome do escolhido .
import random
n1=input('Nome do primero aluno: ')
n2=input('Nome do segundo aluno: ')
n3=input('Nome do terseiro aluno: ')
n4=input('Nome do quarto aluno: ')
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print('Aluno escolhido foi {}'.format(escolhido))