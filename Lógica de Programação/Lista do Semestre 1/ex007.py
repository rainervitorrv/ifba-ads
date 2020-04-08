# O programa lê uma velocidade em km/h e mostra o resultado em m/s
# Autor: Rainer Sousa
# Data: 07/04/2020

velocidadeKm = float(input('Informe a velocidade em KM/H: '))

velocidadeMs = velocidadeKm / 3.6

print('{:.1f} km/h equivalem a {:.2f} m/s'.format(velocidadeKm, velocidadeMs))
