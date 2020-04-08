# O programa lê um número e informa se ele é par ou ímpar
# Autor: Rainer Sousa
# Data: 07/04/2020

numero = int(input('Informe um número: '))

if(numero % 2 == 0 ):
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é impar!'.format(numero))