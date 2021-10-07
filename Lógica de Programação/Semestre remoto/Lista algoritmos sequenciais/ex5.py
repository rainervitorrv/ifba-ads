# Recebe a altura de uma pessoa em metros e exibe o peso ideal baseado na fórmula (72.7*altura) - 58
# Disponível em github.com/rainervitorrv

altura = float(input('Informe a sua altura: '))
pesoIdeal = (72.7 * altura) - 58

print('-------------------------------------------------')
print('ALTURA INFORMADA: {:.2f}m'.format(altura))
print('PESO IDEAL: {:.1f}kg'.format(pesoIdeal))
print('-------------------------------------------------')

