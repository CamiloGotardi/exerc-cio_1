def orcamento_diario(orcamento_total, dias_viagem):
    orcamento_diario = orcamento_total/dias_viagem
    print(f'Olá, o seu orçamento por dia é de R$ {orcamento_diario:.2f}.')


orcamento_total = float(input("Qual o seu orçamento total para a viagem?"))
dias_viagem = int(input("Quantos dias você estará viajando?"))

orcamento_diario(orcamento_total, dias_viagem)