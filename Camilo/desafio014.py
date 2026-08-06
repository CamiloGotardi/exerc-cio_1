#Escreva um programa que converta uma temperatura digitada em °C e converta para °F. 

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))


def converter_temperatura(celsius):
    fahrenheit = ((9 * celsius) / 5) + 32
    return fahrenheit

c = float(input('Informe a temperatura em °C: '))
f = converter_temperatura(c)
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))

