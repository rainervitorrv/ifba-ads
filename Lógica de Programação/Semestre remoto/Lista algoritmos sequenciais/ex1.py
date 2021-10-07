# Calcula e mostra o total do salário no referido mês baseado em
# número de horas trabalhadas x valor recebido por hora trabalhada
# O programa recebe apenas números inteiros no campo referente a qtd de horas trabalhadas
# Disponível em github.com/rainervitorrv 

valorGanhoHora = float(input('Informe o valor que você ganha por hora: '))
totalHorasTrabalhadasMes = int(input('Informe o número de horas trabalhadas no mês: '))

totalSalario = valorGanhoHora * totalHorasTrabalhadasMes

print('-----------------------------------------')
print('VALOR RECEBIDO POR HORA: R$ {:.2f}'.format(valorGanhoHora))
print('TOTAL DE HORAS: {}h'.format(totalHorasTrabalhadasMes))
print('TOTAL A RECEBER: R$ {:.2f}'.format(totalSalario))
print('-----------------------------------------')
