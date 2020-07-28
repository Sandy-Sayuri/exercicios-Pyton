#Faça um programa que leia um número intero qualquer e mostre na tela a sua tabuada.
n1=int(input('Digite um numero :'))
print('A tabuada do número {}'.format(n1))
for i in range (0,11,1):
    print('{} * {} = {}'.format(n1,i,n1*i))