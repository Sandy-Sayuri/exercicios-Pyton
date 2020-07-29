#Faça um programa que leia a altura e largura de uma parede em metros calcule a quantidade de tinta necessária para pintá-lo , sabendo que cada litro de tinta, pinta uma área de 2m2.
a=int(input('Digite a altura da parede: '))
l=int(input('digite a largura da parede: '))
print('você vai preciar de {} latas de tinta'.format((l*a)*2))