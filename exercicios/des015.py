#  Escreva um prigama que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$0.15 por Km rodado.
qkp=int(input('quantidade de Km percorridos: '))
qd=int(input('quantidade de dias com o carro alugado: '))
print('A pessoas vai ter que pagar {}'.format((qd*60)+(qkp*0.15)))