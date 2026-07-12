def converter_idade():
    idade=input('Quantos anos voçê tem?')
    dias=int(idade) * 365
    horas=dias*24
    print(f'Você tem {idade} anos\nEm dias são {dias} dias\nEm horas são {horas} horas')
    #print('Você tem {} anos, em dias são {} dias.'.format(idade, dias))

converter_idade()