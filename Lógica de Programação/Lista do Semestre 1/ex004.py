# O programa calcula o  de valor de uma prestação em atraso e mostra o valor com juros
# Autor: Rainer Sousa
# Data: 05/04/2020

valor = float(input('Informe o valor da prestação em atraso: R$'))
taxa = float(input('Informe a taxa de juros aplicada ao mês. \n--> Digitar somente números: '))
tempo = float(input('Informe o tempo (Mês) de atraso da prestação: '))

prestacao = valor + (valor * (taxa/100) * tempo)
print('O valor da prestação em atraso com a taxas é R${:.2f}'.format(prestacao))

