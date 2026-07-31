#calcule a média de 2 notas.

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = calcular_media(n1, n2)
print(f'A média das notas é: {media:.2f}')

