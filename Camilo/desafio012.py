#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

def calcular_desconto(preco):
    desconto = preco * 0.05
    novo_preco = preco - desconto
    return novo_preco

preco_produto = float(input('Digite o preco do produto: R$ '))
novo_preco = calcular_desconto(preco_produto)
print(f'O novo preço do produto com 5% de desconto é: R$ {novo_preco:.2f}')

