# 2 O Programa verifica se uma letra digitada é vogal ou consoante.

letra = str(input('Informe a letra: ')).lower()

if (len(letra) == 1):
    if (
        letra == 'a'
        or letra == 'e'
        or letra == 'i'
        or letra == 'o'
        or letra == 'u'
    ):
        print('Vogal')
    else:
        print('Consoante')
else:
    print('Por favor, informe uma letra válida')
