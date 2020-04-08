# O programa recebe quatro números e mostra na tela a média ponderada, com os pesos 1, 2, 3 e 4.
# Autor: Rainer Sousa
# Data: 05/04/2020

numero1 = float(input('Informe o 1º número: ')) * 1 
numero2 = float(input('Informe o 2º número: ')) * 2 
numero3 = float(input('Informe o 3º número: ')) * 3 
numero4 = float(input('Informe o 4º número: ')) * 4 
mediaPonderada = (numero1 + numero2 + numero3 + numero4) / (1 + 2 + 3 + 4)

print('Foram informados os seguintes valores: {}, {}, {}, {} \nMédia ponderada: {}'.format(numero1, numero2, numero3, numero4, mediaPonderada))