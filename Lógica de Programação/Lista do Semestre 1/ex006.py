# O programa lê um valor de hora e mostra quantos minutos se passaram desde o inicio do dia.
# Autor: Rainer Sousa
# Data: 07/04/2020

print('Por favor, informe a hora e os minutos')
hora = int(input('Hora: '))
minuto = int(input('Minutos: ')) 
totalMinutos = (hora * 60) + minuto
print('São {}h{}min. \nJá se passaram {} minutos desde o ínicio do dia!'.format(hora, minuto, totalMinutos))