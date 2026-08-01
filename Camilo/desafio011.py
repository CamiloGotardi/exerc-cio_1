#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

def area_parede(largura, altura):
    area = largura * altura
    return area
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = area_parede(largura, altura)

def quantidade_tinta(area):
    tinta_necessaria = area / 2
    return tinta_necessaria
tinta = quantidade_tinta(area)
print(f'A área da parede é de {area:.2f} m² e a quantidade de tinta necessária para pintá-la é de {tinta:.2f} litros.')

