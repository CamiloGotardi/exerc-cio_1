#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

def converter_metros(valor_metros):
    valor_centimetros = valor_metros * 100
    valor_milimetros = valor_metros * 1000
    return valor_centimetros, valor_milimetros

valor_metros = float(input('Digite um valor em metros: '))

valor_centimetros, valor_milimetros = converter_metros(valor_metros)
print(f'O valor em centímetros é: {valor_centimetros:.2f} cm')
print(f'O valor em milímetros é: {valor_milimetros:.2f} mm')

