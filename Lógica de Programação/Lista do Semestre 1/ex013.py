# O programa calcula o Imposto de Renda a ser pago
# Autor: Rainer Sousa
# Data: 07/04/2020

salario = float(input('Informe o seu sálario: '))

if(salario < 901):
    print('Você é ISENTO do pagamento do IR')
    exit()
elif(salario < 1801):
    print('Você deverá pagar uma aliquota de 15% de IR, totalizando R${:.2f}'.format(salario * 0.15))
    exit()
else:
    print('Você deverá pagar uma aliquota de 20% de IR, totalizando R${:.2f}'.format(salario * 0.2))