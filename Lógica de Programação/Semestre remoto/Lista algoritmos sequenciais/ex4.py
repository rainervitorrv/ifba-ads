# O programa recebe dois números inteiros e um real e informa:
# O produto do dobro do primeiro com metade do segundo
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.
# Disponível em github.com/rainervitorrv

primeiroInteiroRecebido = int(input('Infome o primeiro número inteiro: '))
segundoInteiroRecebido = int(input('Informe o segundo número inteiro: '))
numeroRealRecebido = float(input('Informe o número com o valor real: '))

print('-----------------------------------------------------------------')
print('PRODUTO DO DOBRO DE {} COM A METADE DE {}:  {}'.format(
    primeiroInteiroRecebido,
    segundoInteiroRecebido,
    (primeiroInteiroRecebido * 2) + (segundoInteiroRecebido / 2)))
print('-----------------------------------------------------------------')
print('SOMA DO TRIPLO DE {} COM {}:  {}'.format(
    primeiroInteiroRecebido,
    numeroRealRecebido,
    (primeiroInteiroRecebido * 3) + numeroRealRecebido
))
print('-----------------------------------------------------------------')
print('{} ELEVADO AO CUBO:  {}'.format(numeroRealRecebido, numeroRealRecebido**3))
print('-----------------------------------------------------------------')
