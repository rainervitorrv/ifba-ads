# O programa recebe a temperatura em graus Fahrenheit e transforme/mostra a temperatura em graus Celsius
# Disponível em github.com/rainervitorrv

temperaturaFahrenheit = int(input('Informe a temperatura em graus Fahrenheit: '))

temperaturaCelsius = 5 * ((temperaturaFahrenheit - 32) / 9)

print('-----------------------------------------------------------------')
print('TEMPERATURA RECEBIDA: {} ºF'.format(temperaturaFahrenheit))
print('TEMPERATURA CONVERTIDA EM GRAUS CELSIUS: {:.1f} ºC'.format(temperaturaCelsius))
print('-----------------------------------------------------------------')