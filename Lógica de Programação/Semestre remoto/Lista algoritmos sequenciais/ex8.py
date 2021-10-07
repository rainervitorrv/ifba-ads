# O programa recebe o valor ganho por hora e o número de horas trabalhadas no mês e mostra
# o total do sálario do referido mês
# Disponível em github.com/rainervitorrv

valorGanhoHora = float(input('Informe o valor recebido por hora: '))
horasTrabalhadasMes = int(input('Informe o total de horas trabalhadas: '))

salarioBruto = valorGanhoHora * horasTrabalhadasMes
descontoINSS = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05
descontoIR = salarioBruto * 0.11
totalDescontado = descontoINSS + descontoIR + descontoSindicato

print('-------------------------------------------------')
print('SALÁRIO BRUTO: R$ {:.2f}'.format(salarioBruto))
print('VALOR PAGO INSS: R$ {:.2f}'.format(descontoINSS))
print('VALOR PAGO AO SINDICATO: R$ {:.2f}'.format(descontoSindicato))
print('VALOR PAGO IR: R$ {:.2f}'.format(descontoIR))
print('VALOR TOTAL DESCONTADO: R$ {:.2f}'.format(totalDescontado))
print('SALÁRIO LIQUIDO: R$ {:.2f}'.format(salarioBruto - totalDescontado))
print('-------------------------------------------------')