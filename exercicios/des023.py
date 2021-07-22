#faça um programa que leia um numero de 0 a 9999 e mostre na tele cada um dos digitos
num=int (input('digite um numero:'))
u= num // 1 % 10
d= num //10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print(f'analizando o numero {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')