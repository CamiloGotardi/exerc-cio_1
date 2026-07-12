def area_retangulo(altura, largura):
    print("Vamos calcular a área de um retangulo!")
    area=largura*altura
    print("A área do retângulo é: {}".format(area))


altura=float(input("Digite a altura do retângulo:"))
largura=float(input("Digite a largura do retângulo:"))

area_retangulo(altura, largura)