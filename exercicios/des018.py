#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno,cosseno e tangente desse ângulo
import math
a=int(input('Digite um ângulo : '))
seno=math.sin(math.radians(a))
cos=math.cos(math.radians(a))
tang=math.tan(math.radians(a))
print('O seno do ângulo {:.2f}\n Cosseno : {} \nTangente:{}'.format(seno,cos,tang))
