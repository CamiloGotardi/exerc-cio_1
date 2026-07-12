def exibir_esporte(nome, esporte):
    print(f'Olá, {nome}, seu esporte favorito é {esporte}!')

def get_information():
    nome = input("Olá, digite o seu nome:")
    esporte = input("Digite o seu esporte favorito:")
    exibir_esporte(nome, esporte)


get_information()
