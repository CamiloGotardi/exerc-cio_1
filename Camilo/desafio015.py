#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0,15 por km rodado.

km = float(input('Informe a quantidade de km percorridos: '))
dias = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))
preco = (dias * 60) + (km * 0.15)
print('O preço a pagar pelo aluguel do carro é de R${:.2f}'.format(preco))

def calcular_preco_aluguel(km, dias):
    preco = (dias * 60) + (km * 0.15)
    return preco

km = float(input('Informe a quantidade de km percorridos: '))
dias = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))
preco = calcular_preco_aluguel(km, dias)
print('O preço a pagar pelo aluguel do carro é de R${:.2f}'.format(preco))

