# O programa recebe a altura de uma pessoa(em metros) e calcula o peso ideal utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# Disponível em github.com/rainervitorrv

altura = float(input('Informe a sua altura: '))

pesoIdealHomem = (72.7 * altura) - 58
pesoIdealMulher = (62.1 * altura) - 44.7

print('-------------------------------------------------')
print('ALTURA INFORMADA: {:.2f}m'.format(altura))
print('PESO IDEAL PARA O HOMEM: {:.1f}kg'.format(pesoIdealHomem))
print('PESO IDEAL PARA A MULHER: {:.1f}kg'.format(pesoIdealMulher))
print('-------------------------------------------------')


