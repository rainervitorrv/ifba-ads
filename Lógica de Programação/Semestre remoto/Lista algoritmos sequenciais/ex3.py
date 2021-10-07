# O programa recebe a temperatura em graus Celsius e transforme/mostra a temperatura em graus Fahrenheit
# Disponível em github.com/rainervitorrv

temperaturaCelsius = int(input('Informe a temperatura em graus Celsius: '))

temperaturaFahrenheit = ((temperaturaCelsius * 9 / 5) + 32)

print('-----------------------------------------------------------------')
print('TEMPERATURA RECEBIDA: {} ºC'.format(temperaturaCelsius))
print('TEMPERATURA CONVERTIDA EM GRAUS FAHRENHEIT: {:.1f} ºF'.format(temperaturaFahrenheit))
print('-----------------------------------------------------------------')