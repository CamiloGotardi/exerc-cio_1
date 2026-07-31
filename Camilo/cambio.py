def real_euro(valor):
    Real = valor / 5.78
    return Real

valor = float(input('Digite o valor em real:'))
resultado = real_euro(valor)
print(f'O valor em euro é: {resultado:.2f}')

