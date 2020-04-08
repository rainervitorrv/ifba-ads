# O programa recebe o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e calcula
# O valor em reais de cada quilowatts
# O valor total
# O valor em reais a ser pago o novo valor a ser pago, considerando um desconto de 10%
# Autor: Rainer Sousa
# Data: 07/04/2020

salarioMinimo = float(input('Informe o valor do sálario mínimo: '))
quantidadeKw = float(input('Informe o total de quilowatts gasto na sua residência: '))

valorKw = (salarioMinimo * (1/7)) * (quantidadeKw / 100) / quantidadeKw 
valorTotal = (salarioMinimo * (1/7)) * (quantidadeKw / 100) 
valorComDesconto = valorTotal - valorTotal * 0.1 

print('-' * 40)
print('O Valor do Sálario Mínimo informado foi R${:.2f} e o consumo de energia foi {} quilowatts'.format(salarioMinimo, quantidadeKw))
print('O valor em reais para cada quilowatts é R${:.2f}'.format(valorKw))
print('O valor total é R${:.2f}'.format(valorTotal))
print('Com um desconto de 10% você pagará R${:.2f}'.format(valorComDesconto))
