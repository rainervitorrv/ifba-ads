# O programa informa se um empréstimo poderá ou não ser concedido
# # Autor: Rainer Sousa
# Data: 07/04/2020

salarioBruto = float(input('Informe o seu sálario bruto: '))
valorDaPrestacao = float(input('Informe o valor da prestação: '))

if(valorDaPrestacao <= salarioBruto * 0.3):
    print('Parabéns!!! O empréstimo foi concedido!')
else:
    print('Desculpe, não foi dessa vez. O empréstimo não foi concedido.')