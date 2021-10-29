
print('Informe o turno que você estuda:')
print(
    'Digite: M => Matutino | '
    'V => Vespertino | '
    'N => Noturno'
)
turno = str(input('Digite a opção: ')).upper()

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
