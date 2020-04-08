# Recebe dois valores (inteiros positivos) e determina quem é o maior em relacão ao outro
# Autor: Rainer Sousa
# Data: 07/04/2020

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

if(valor1 > valor2):
    print('{} é maior do que {}'.format(valor1, valor2))
elif(valor2 > valor1):
    print('{} é maior do que {}'.format(valor2, valor1))
else:
    print('Ambos são iguais!')