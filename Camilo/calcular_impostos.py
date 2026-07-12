#salario=float(input("Digite o seu salário:"))
#imposto=salario*0.275
#print(imposto)



def calcular_imposto(salario):
    if salario > 10000:
        return salario * 0.275

imposto = calcular_imposto(10001)
print(imposto)
