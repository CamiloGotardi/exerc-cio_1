#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27

def real_dolar():
    real = float(input('Digite quanto dinheiro você tem na carteira em reais: '))
    dolar = real / 3.27
    print(f'Com R${real:.2f}, você pode comprar US${dolar:.2f}.')
print(real_dolar())
