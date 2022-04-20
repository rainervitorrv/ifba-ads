maiorNumero = 0

for i in range(5):
    numero = float(input('Infome o {}º número: '.format(i+1)))
    if numero > maiorNumero:
        maiorNumero = numero
print('O maior número informado foi: ', maiorNumero)
