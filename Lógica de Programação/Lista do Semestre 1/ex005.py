# O programa lê o numerador e denominador de uma fração e transforma em decimal.
# Autor: Rainer Sousa
# Data: 05/04/2020

numerador = int(input('Informe o numerador: '))
denominador = int(input('Informe o denominador: '))

conversaoDecimal = numerador / denominador
print('A conversão dos núemros para decimal resultou em {}'.format(conversaoDecimal))