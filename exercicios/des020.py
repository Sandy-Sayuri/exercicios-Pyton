#O mesmo professor do desafio anterior quer sortear a ordem de trabalho dos alunos. Faço um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
n1=input('Nome do primero grupo: ')
n2=input('Nome do segundo grupo: ')
n3=input('Nome do terceiro grupo: ')
n4=input('Nome do quarto grupo: ')
lista=[n1,n2,n3,n4]
shuffle(lista)
print('A ordem será {}'.format(lista))