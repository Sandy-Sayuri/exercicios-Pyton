#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas e minúsculas.
#-Quantas letras ao todo(sem considerar espaços).
#-Quantas letras tem o primero nome. 
nome=str(input("digite um nome:")).strip()
print('Analizando nome...')
print('Seu nome em maiuscula é {}'.format(nome.upper()))
print('Seu nome em manuscula é {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))#o quanto tem de carcteres - o espaço
print('Seu primeiro nome tem {}'.format(nome.find(' ')))