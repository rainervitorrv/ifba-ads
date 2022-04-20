
while True:
    nome = str(input('Informe o nome: ')).strip()
    if len(nome) > 3:
        while True:
            idade = int(input('Informe a idade: '))
            if idade >= 0 and idade <= 150:
                while True:
                    salario = float(input('Informe o salário: '))
                    if salario > 0:
                        while True:
                            sexo = str(input('Informe o sexo: ')).lower()
                            if sexo.strip() == 'f' or sexo.strip() == 'm':
                                while True:
                                    estadoCivil = str(
                                        input('Informe o estado civil: ')).lower()
                                    if (
                                        estadoCivil.strip() == 's' or
                                        estadoCivil.strip() == 'c' or
                                        estadoCivil.strip() == 'v' or
                                        estadoCivil.strip() == 'd'
                                    ):
                                        break
                                    print('Estado civil inválido!')
                                break
                            print('Sexo inválido!')
                        break
                    print('Salário inválido!')
                break
            print('Idade inválida')
        break
    print('Nome inválido')
