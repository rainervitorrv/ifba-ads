# O programa recebe o peso(peso de peixes) e calcula o excendente de quilos(além do limite permitido)
# Mostra a multa a pagar pelo excedente de peso.
# Disponível em github.com/rainervitorrv

LIMITE_MAXIMO_KG = 50
VALOR_MULTA_KG = 4

pesoPeixes = float(input('Informe a quantidade de peixes em KG: '))

excessoPeso = pesoPeixes - LIMITE_MAXIMO_KG
excessoPeso = 0 if excessoPeso <= 0 else excessoPeso  
valorMulta = excessoPeso * VALOR_MULTA_KG

print('-------------------------------------------------')
print('QUANTIDADE INFORMADA DE PEIXES: {:.2f} kg'.format(pesoPeixes))
print('EXCESSO DE PESO: {:.2f} kg'.format(excessoPeso)) 
print('VALOR DA MULTA: R$ {:.2f}'.format(valorMulta))
print('-------------------------------------------------')