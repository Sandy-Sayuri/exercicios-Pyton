n1=int(input('digite um número: '))
n2= int(input('digite outro numero: '))
s=n1+n2
m=n1*n2
e=n1**n2
if(n1>n2):
    d=n1/n2
    di=n1//n2
    su=n1-n2
else:
    d=n2/n1
    di=n2//n1
    su=n2-n1
print('A soma é {},o produto é {} e a potência {}'.format(s,m,e))
print('Divisão {}, Divisão intera {} e Subtração {}'.format(d,di,su) ,end='')