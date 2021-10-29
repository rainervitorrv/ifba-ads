valorHora = float(input('Informe o valor da hora: '))
quantidadeHorasTrabalhadas = int(
    input('Informe a quantidade de horas trabalhadas: '))

salarioBruto = valorHora * quantidadeHorasTrabalhadas

if salarioBruto <= 900:
    percentualIR = 0
    descontoIR = 0
elif salarioBruto <= 1500:
    percentualIR = 5
    descontoIR = salarioBruto * 0.05
elif salarioBruto <= 2500:
    percentualIR = 10
    descontoIR = salarioBruto * 0.1
else:
    percentualIR = 20
    descontoIR = salarioBruto * 0.2


descontoSindicato = salarioBruto * 0.03
descontoINSS = salarioBruto * 0.1
descontoFGTS = salarioBruto * 0.11
totalDescontos = descontoFGTS + descontoIR + descontoSindicato
salarioLiquido = salarioBruto - totalDescontos

print('Salário Bruto: (R$ {:.2f} * {}) : R$ {:.2f}'.format(valorHora,
      quantidadeHorasTrabalhadas, salarioBruto))
print('(-) IR ({}%): R$ {:.2f}'.format(percentualIR, descontoIR))
print('(-) INSS (10%): R$ {:.2f}'.format(descontoINSS))
print('(-) Sindicato (3%): R$ {:.2f}'.format(descontoSindicato))
print('FGTS (11%): R$ {:.2f}'.format(descontoFGTS))
print('Total de descontos: R$ {:.2f}'.format(totalDescontos))
print('Salario Liquido: R$ {:.2f}'.format(salarioLiquido))
