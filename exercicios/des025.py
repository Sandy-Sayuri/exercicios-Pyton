# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome= str(input('Qual é seu nome completo? ')).split()
print('seu nome tem Silva {}'.format('silva' in nome.lower()))