# O programa recebe o tamanho em metros quadrados(valor inteiro) da área a ser pintada e informa ao usuário
# a quantidades de latas de tinta a serem compradas e o preço total.
# A cobertura da tinta é de 1 litro para cada 3 metros quadrados e a tinta é vendida em latas de 18 litros
# e custam R$ 80,00
# Disponível em github.com/rainervitorrv

tamanhoAreaSerPintada = int(input('Informe o tamanho da área a ser pintada: '))

qtdLitrosTintaNecessario = tamanhoAreaSerPintada / 3
qtdLatasTintaNecessario = qtdLitrosTintaNecessario / 18
qtdLatasTintaNecessario = 1 if qtdLitrosTintaNecessario < 18 else qtdLatasTintaNecessario
precoTotal = qtdLatasTintaNecessario * 80

print('-------------------------------------------------')
print('TAMANHO DA ARÉA A SER PINTADA: {:.0f}m²'.format(tamanhoAreaSerPintada))
print('QUANTIDADE DE LITROS DE TINTA GASTO: {:.0f}l'.format(qtdLitrosTintaNecessario))
print('QUANTIDADE DE LATAS QUE DEVE SER COMPARADA: {:.0f} LATAS'.format(qtdLatasTintaNecessario))
print('VALOR TOTAL A SER GASTO: R$ {:.2f}'.format(precoTotal))
print('-------------------------------------------------')

