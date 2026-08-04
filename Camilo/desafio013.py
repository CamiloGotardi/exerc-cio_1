#Faça um algoritmo que leia o salário de um funcionáro e mostre seu novo salário, com 15% de aumento.

def calcular_novo_salario(salario):
    aumento = salario * 0.15
    novo_salario = salario + aumento
    return novo_salario

salario_atual = float(input('Digite o salário do funcionário: R$ '))
novo_salario = calcular_novo_salario(salario_atual)
print(f'O novo salário do funcionário, com 15% de aumento, será: R$ {novo_salario:.2f}')

s = float(input('Digite o salário do funcionário: R$ '))
calculo = float(input('Digite o percentual de aumento (em %): '))
novo_salario = s + (s * (calculo / 100))
print('O novo salário do funcionário, com {}% de aumento, será: R$ {:.2f}'.format(calculo, novo_salario))

